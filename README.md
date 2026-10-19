# Local Telecom Data Project (`telecom-edge-dw`)

Hi, I'm Mackay. This is a personal practice project I built to learn how data moves from a messy, raw state into clean tables that can run a business dashboard. I wanted to simulate how data pipelines work in real enterprises, using tools I can run entirely on my local machine.

## My Profile & Goals
* **About Me:** Graduate Support Officer at Datec PNG Limited (working with Pronto XI ERP Systems Support).
* **Education:** B.Sc. in Mathematics, Statistics, and Computer Science.
* **Why I Built This:** I want to transition into roles like Data Engineering or Database Architecture. This project bridges what I learned in university with practical database patterns.

---

## Skills I Am Actively Mastering
To build on my university background and my current systems support experience, I am using this repository as a sandbox to learn and master these foundational skills:
* **SQL & Relational Database Design:** Practicing relational schemas by writing SQL queries to transform staging data into a **Star Schema** layout (structuring data into `fact_invoices`, `dim_customers`, and `dim_plans` tables).
* **Linux & CLI Environments:** Moving away from Windows interfaces to run and manage Python script automation jobs directly through standard command-line environments.
* **Pipeline Automation:** Writing master orchestration routines that link single scripts together so data loads smoothly end-to-end without manual adjustments.
* **Python for Data Pipelines:** Using structural libraries like `Pandas` to clean complex text errors, manage bad input data, and enforce financial data quality gates.

---

## How this Project Maps to Big-Company Systems
Since I don't have corporate cloud access at home, I used open-source and local tools to mimic how major systems process information:

| What I Used Locally | What Large Enterprises Use | What it Does in this Project |
| :--- | :--- | :--- |
| Python + `Faker` | Operational Databases | Creates fake, messy telco transaction files with errors to simulate real-world data entry. |
| Local Folders (`data/raw/`) | Cloud Storage (AWS S3 / Azure) | A safe landing zone where the untouched CSV files are saved first. |
| Python + `Pandas` | Transformation Tools (dbt / Spark)| My cleanup scripts. It fixes text errors, handles missing rows, and filters out bad records. |
| SQLite Data Warehouse (`database/`) | Cloud Data Warehouses | My relational database where clean staging records are transformed into final Star Schema tables using SQL queries. |
| Power BI Desktop | Power BI Cloud / Tableau | Connects directly to my clean dataset to create charts for business reviews. |

---

## My Rules for Cleaning the Data
Instead of just deleting broken rows, I wanted to practice safe financial data handling:
1. **The Isolation Bin (Quarantine):** If an invoice is completely missing its ID (`invoice_id`), my script moves it to a separate table called `error_quarantine_invoices` so it isn't lost but doesn't ruin the main reports.
2. **Filling Missing Information:** If a customer name or region is blank, the script automatically replaces it with a placeholder like `Walk-in Customer` or `CUST-UNKNOWN` so totals don't get miscounted.
3. **Standardizing Text:** I used Python to strip whitespace and force categories (like prepaid vs. postpaid) to `UPPERCASE` so typos don't create accidental duplicate categories.

---

## What the Business Dashboard Tracks
I hooked up my clean processed dataset directly to **Power BI Desktop** to build an executive report tracking performance in Papua New Guinea. Based on my current run, the data shows:
* **Total Revenue (Card):** Displays an overall total revenue figure of **50.89K**.
* **Regional Sales (Donut Chart):** Breaks down income between our major hubs—the **Momase Region (Lae) at 27.58K (54.19%)** and the **Southern Region (POM) at 23.31K (45.81%)**. 
* **Plan Popularity (Bar Chart):** Shows which subscription packages are driving the most value, led prominently by *POSTPAID UNLIMITED* and *PREPAID BASIC*.
* **Payment Health (Trend Line):** Evaluates accounts receivable status across chronological timelines, tracking distributions for invoices marked as *OVERDUE*, *PAID*, *PENDING*, or *UNKNOWN*.

_A visual snapshot of my executive report dashboard can be seen inside the `docs/reporting_dashboard.png` file._

---

## Project Structure & Tree
```text
telecom-edge-dw/
├── data/
│   ├── processed/          # Holds clean data dumps (master_clean_traffic.csv)
│   └── raw/                # Holds messy initial outputs (master_raw_traffic.csv)
├── database/               # Relational database folder containing telecom_warehouse.db
│                           # (Tables: analytics_cleaned_invoices, dim_customers, dim_plans, fact_invoices)
├── docs/                   # Visual project reports (reporting_dashboard.png)
├── src/                    # Core Python pipeline scripts
├── pipeline_runner.ipynb   # Master notebook orchestration file
├── README.md               # Project documentation
└── requirements.txt        # Third-party package installations
```

---

## How to Run It Locally

1. **Clone the Project:**
   ```bash
   clone https: https://github.com/mackay-iria/telecom-edge-dw.git
   cd telecom-edge-dw
   ```

2. **Install Packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Code:**
   Open the `pipeline_runner.ipynb` control center file using Jupyter to execute the generation, data cleaning, and SQL database loading routines sequentially.
