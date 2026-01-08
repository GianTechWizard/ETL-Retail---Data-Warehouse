# ETL-Retail---Data-Warehouse

HOW TO RUN

**1. Install dependencies**
   pip install -r requirements.txt

**2. Configure database**
   Edit file configure/db_config.py:

   DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "retail_dw",
    "user": "postgres",
    "password": "your_password"
}

**4. Run ETL pipeline**
   python main.py

   ETL akan:
   * Extract data dari CSV
   * Transform ke Star Schema
   * Load ke PostgreSQL Data Warehouse

  **Output**
  PostgreSQL tables:
  - fact_sales
  - dim_customer
  - dim_product
  - dim_time

  CSV hasil ETL tersedia di folder data/processed/

  **Dashboard**
  Data dianalisis dan divisualisasikan menggunakan Looker Studio, berikut ini:
  https://lookerstudio.google.com/reporting/dac9f992-9b52-4cb8-b5e1-d44f0ff53f9c  

  **Author**
  Gian Ananta Koleba - Data Engineering (Academic Project)
