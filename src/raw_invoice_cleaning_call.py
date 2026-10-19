import sys
import os
from datetime import datetime

# Include src directory in search path to import sibling script files safely
sys.path.append(os.path.dirname(__file__))
import raw_invoice_cleaning

PROJECT_ROOT = r"C:\Users\Mackay Iria\DataMiningProjects\telecom-edge-dw"

# Allows passing an explicit date argument or defaults to today
target_run_date = sys.argv[1] if len(sys.argv) > 1 else datetime.today().strftime('%Y-%m-%d')

print(f"\n--- INITIATING RUN: CLEANING & LOAD FOR {target_run_date} ---")
raw_invoice_cleaning.execute_cleaning_and_load(PROJECT_ROOT, target_run_date)
