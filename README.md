# Local Telecom Data Project (`telecom-edge-dw`)

Hi, I'm Mackay. This is a personal practice project I built to learn how data moves from a messy state into clean tables for a business dashboard, mimicking enterprise data pipelines using local tools.

## My Profile & Goals
* **About Me:** Graduate Support Officer at Datec PNG Limited (Pronto XI ERP Systems Support).
* **Education:** B.Sc. in Mathematics, Statistics, and Computer Science.
* **Why I Built This:** To transition into Data Engineering or Database Architecture by bridging university learning with practical database patterns.

---

## Skills I Am Actively Mastering
* **SQL & Relational Design:** Structuring data into Star Schema layouts (`fact_invoices`, `dim_customers`, `dim_plans`).
* **Linux & CLI:** Managing automation tasks via command-line terminals instead of Windows interfaces.
* **Pipeline Automation:** Linking scripts together for smooth end-to-end data loading.
* **Python for Data Pipelines:** Using Pandas to clean text errors and manage records.

---

## Enterprise Mapping

| Local Tool | Enterprise Equivalent | Project Role |
| :--- | :--- | :--- |
| Python + `Faker` | Operational DBs | Generates messy transaction files with simulated errors. |
| Local Folders (`data/raw/`) | Cloud Storage (S3/Azure) | Landing zone for untouched CSV files. |
| Python + `Pandas` | Transformation Tools (dbt/Spark)| Cleans text and filters bad records. |
| SQLite (`database/`) | Cloud Data Warehouses | Relational storage for final Star Schema tables. |
| Power BI Desktop | Power BI Cloud/Tableau | Visualizes clean datasets for reports. |

---

## Data Cleaning Rules
1. **Quarantine:** Moves missing `invoice_id` records to `error_quarantine_invoices`.
2. **Placeholders:** Replaces blank customer names/regions with defaults like `Walk-in Customer`.
3. **Standardizing Text:** Strips whitespace and forces categories to uppercase.

---

## Dashboard Tracking
Connected to Power BI Desktop for Papua New Guinea performance tracking:
* **Total Revenue:** **50.89K**
* **Regional Sales:** Momase Region (Lae) at 27.58K (54.19%) and Southern Region (POM) at 23.31K (45.81%).
* **Plan Popularity:** Led by *POSTPAID UNLIMITED* and *PREPAID BASIC*.
* **Payment Health:** Tracks invoice states (*OVERDUE*, *PAID*, *PENDING*, *UNKNOWN*).

---

## Project Structure
```text
telecom-edge-dw/
├── data/ (processed/, raw/)
├── database/ (telecom_warehouse.db)
├── docs/ (reporting_dashboard.png)
├── src/
├── pipeline_runner.ipynb
├── README.md
└── requirements.txt
```

---

## How to Run It Locally
1. **Clone the Project:**
   ```bash
   git clone https://github.com/mackay-iria/telecom-edge-dw.git
   cd telecom-edge-dw
   ```
2. **Install Packages:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Code:** Open `pipeline_runner.ipynb` in Jupyter to run the routines sequentially.
