import os
import sqlite3
import pandas as pd

def execute_cleaning_and_load(project_root, target_date_str):
    master_raw_path = os.path.join(project_root, "data", "raw", "master_raw_traffic.csv")
    master_clean_path = os.path.join(project_root, "data", "processed", "master_clean_traffic.csv")
    db_path = os.path.join(project_root, "database", "telecom_warehouse.db")
    
    if not os.path.exists(master_raw_path):
        print("Cleaning cancelled: Master raw data file does not exist yet.")
        return
        
    # Read global log
    full_df = pd.read_csv(master_raw_path)
    
    # Incremental Slice Isolation
    incremental_df = full_df[full_df['invoice_date'] == target_date_str].copy()
    
    if incremental_df.empty:
        print(f"Warning: No raw transactions found matching date: {target_date_str}")
        return
        
    print(f"[CLEANER] Isolating {len(incremental_df)} rows for processing slice.")
    
    # =========================================================================
    # DATA QUALITY STRATEGY (No Data Loss)
    # =========================================================================
    
    # 1. Quarantine completely broken records (Missing critical Invoice ID)
    quarantine_mask = incremental_df['invoice_id'].isna()
    quarantine_df = incremental_df[quarantine_mask].copy()
    
    # Keep only records that have a valid Invoice ID for the clean layer
    valid_df = incremental_df[~quarantine_mask].copy()
    
    # 2. Fill Missing Customer Attributes instead of dropping them
    valid_df['customer_id'] = valid_df['customer_id'].fillna('CUST-UNKNOWN-RETAIL')
    valid_df['customer_name'] = valid_df['customer_name'].fillna('Walk-in Customer')
    valid_df['customer_email'] = valid_df['customer_email'].fillna('no-email@vodafone.com.pg')
    
    # Standard text cleaning transformations
    valid_df['plan_type'] = valid_df['plan_type'].str.upper().str.strip()
    valid_df['payment_status'] = valid_df['payment_status'].fillna('UNKNOWN').str.upper().str.strip()
    
    # Parse unstructured names safely
    valid_df['first_name'] = valid_df['customer_name'].apply(lambda x: x.split()[0] if isinstance(x, str) and len(x.split()) > 0 else "Walk-in")
    valid_df['last_name'] = valid_df['customer_name'].apply(lambda x: " ".join(x.split()[1:]) if isinstance(x, str) and len(x.split()) > 1 else "Customer")
    
    analytics_columns = [
        "invoice_id", "invoice_date", "customer_id", "first_name", "last_name", 
        "customer_email", "region", "plan_type", "total_invoice_amount", "payment_status", "payment_method"
    ]
    clean_increment_df = valid_df[analytics_columns]
    
    # Save/Append clean records to the master processed file for Power BI
    clean_exists = os.path.exists(master_clean_path)
    clean_increment_df.to_csv(master_clean_path, mode='a', index=False, header=not clean_exists)
    print(f"[CLEANER] Clean rows appended directly to master file -> {master_clean_path}")
    
    # Load into SQLite Database Layers
    conn = sqlite3.connect(db_path)
    
    # A) Store the raw increment completely unchanged
    incremental_df.astype(str).to_sql("raw_ingested_invoices", conn, if_exists="append", index=False)
    
    # B) Store the pristine clean analytical metrics
    clean_increment_df.to_sql("analytics_cleaned_invoices", conn, if_exists="append", index=False)
    
    # C) Store quarantined failures if they exist so engineers can audit them
    if not quarantine_df.empty:
        quarantine_df.astype(str).to_sql("error_quarantine_invoices", conn, if_exists="append", index=False)
        print(f"[QUARANTINE] Sent {len(quarantine_df)} broken records to 'error_quarantine_invoices' table.")
        
    conn.close()
    print(f"[WAREHOUSE] Data slice processing complete.")
