from connection import start_engine
import pandas as pd
from sqlalchemy import text
from truncate import truncate_table
from extract import extract_data
from load import load_table
import logging
import logs
from exec_procedure import execute_procedure
from datetime import datetime
from dashboard import generate_dashboard


try:
    etl_start_time = datetime.now()

    datasets = [
        {
            "file_path": r"C:\Project_2\data_warehouse_project\datasets\source_crm\cust_info.csv",
            "table_name": "crm_cust_info"
        },
        {
            "file_path": r"C:\Project_2\data_warehouse_project\datasets\source_crm\prd_info.csv",
            "table_name": "crm_prd_info"
        },
        {
            "file_path": r"C:\Project_2\data_warehouse_project\datasets\source_crm\sales_details.csv",
            "table_name": "crm_sales_details"
        },
        {
            "file_path": r"C:\Project_2\data_warehouse_project\datasets\source_erp\CUST_AZ12.csv",
            "table_name": "erp_cust_az12"
        },
        {
            "file_path": r"C:\Project_2\data_warehouse_project\datasets\source_erp\LOC_A101.csv",
            "table_name": "erp_loc_a101"
        },
        {
            "file_path": r"C:\Project_2\data_warehouse_project\datasets\source_erp\PX_CAT_G1V2.csv",
            "table_name": "erp_px_cat_g1v2"
        }
    ]

    # engine ready to connect
    engine = start_engine()

    print("=" * 80)
    print("ETL PROCESS STARTED")
    print("=" * 80)
    logging.info("=" * 80)
    logging.info("ETL PROCESS STARTED")
    logging.info("=" * 80)

    for d in datasets:
        file_path = d["file_path"]
        table_name = d["table_name"]
        source_table_name = table_name.replace("erp_", "").replace("crm_", "")

        print("-" * 80)
        print(f"Processing table: bronze.{table_name}")
        print("-" * 80)

        logging.info("-" * 80)
        logging.info(f"Processing table: bronze.{table_name}")
        logging.info(f"Source file: {file_path}")
        logging.info("-" * 80)

        table_processing_start_time = datetime.now()

        # Extract
        print(f"[EXTRACT] Reading data from {source_table_name}.csv ...")
        logging.info(f"[EXTRACT] Reading data from {source_table_name}.csv ...")

        df = extract_data(file_path)

        print(f"[SUCCESS] Data extracted from {source_table_name}.csv")
        print(f"[INFO] Total rows extracted: {len(df)}")
        print(f"[INFO] Total columns extracted: {len(df.columns)}")

        logging.info(f"[SUCCESS] Data extracted from {source_table_name}.csv")
        logging.info(f"[INFO] Total rows extracted: {len(df)}")
        logging.info(f"[INFO] Total columns extracted: {len(df.columns)}")
        logging.info(f"[PREVIEW] First 5 rows from {source_table_name}.csv:\n{df.head().to_string()}")

        # Truncate
        print(f"[TRUNCATE] Truncating bronze.{table_name} ...")
        logging.info(f"[TRUNCATE] Truncating bronze.{table_name} ...")

        truncate_table(table_name)

        print(f"[SUCCESS] bronze.{table_name} truncated successfully.")
        logging.info(f"[SUCCESS] bronze.{table_name} truncated successfully.")

        # Load
        print(f"[LOAD] Loading data into bronze.{table_name} ...")
        logging.info(f"[LOAD] Loading data into bronze.{table_name} ...")

        load_table(df, table_name, engine)

        print(f"[SUCCESS] Data loaded into bronze.{table_name}")
        logging.info(f"[SUCCESS] Data loaded into bronze.{table_name}")

        # Validate
        print(f"[VALIDATION] Checking row count in bronze.{table_name} ...")
        logging.info(f"[VALIDATION] Checking row count in bronze.{table_name} ...")

        query = pd.read_sql(f"SELECT COUNT(*) FROM bronze.{table_name}", engine)
        row_count = query.iloc[0,0]
        print(f"[INFO] Row count after load for bronze.{table_name}: {row_count}\n")
        logging.info(f"[INFO] Row count after load for bronze.{table_name}: {row_count}")

        table_processing_end_time = datetime.now()
        table_processing_duration = table_processing_end_time - table_processing_start_time
        print(f"[TIME] Table load duration for {table_name} is {table_processing_duration} seconds")
        logging.info(f"[TIME] Table load duration for {table_name} is {table_processing_duration} seconds")

    print("=" * 50)
    print("Bronze Layer Load Completed")
    print("=" * 50)

    # ==================================================
    # SILVER LAYER
    # ==================================================

    print("=" * 50)
    print("Starting Silver Layer Load")
    print("=" * 50)

    execute_procedure(engine, "silver.load_silver")

    print("=" * 50)
    print("Silver Layer Load Completed")
    print("=" * 50)

    # ==================================================
    # GOLD LAYER
    # ==================================================

    print("=" * 50)
    print("Validating Gold Layer")
    print("=" * 50)

    logging.info("=" * 50)
    logging.info("Validating Gold Layer")
    logging.info("=" * 50)

    # dim_customers
    df = pd.read_sql("SELECT COUNT(*) FROM gold.dim_customers", engine)
    row_count = df.iloc[0, 0]

    print(f"gold.dim_customers rows: {row_count}")
    logging.info(f"gold.dim_customers rows: {row_count}")

    # dim_products
    df = pd.read_sql("SELECT COUNT(*) FROM gold.dim_products", engine)
    row_count = df.iloc[0, 0]

    print(f"gold.dim_products rows: {row_count}")
    logging.info(f"gold.dim_products rows: {row_count}")

    # fact_sales
    df = pd.read_sql("SELECT COUNT(*) FROM gold.fact_sales", engine)
    row_count = df.iloc[0, 0]

    print(f"gold.fact_sales rows: {row_count}")
    logging.info(f"gold.fact_sales rows: {row_count}")

    # Dashboard
    print("generating excel dashboard")
    generate_dashboard(engine)

    print("=" * 80)
    print("ETL PROCESS COMPLETED SUCCESSFULLY")
    print("=" * 80)
    
    logging.info("=" * 80)
    logging.info("ETL PROCESS COMPLETED SUCCESSFULLY")
    logging.info("=" * 80)

    etl_end_time = datetime.now()

    print(f"etl_start_time: {etl_start_time}")
    logging.info(f"etl_start_time: {etl_start_time}")

    print(f"etl_end_time: {etl_end_time}")
    logging.info(f"etl_end_time: {etl_end_time}")

    etl_duration = etl_end_time - etl_start_time
    print(f"etl_duration: {etl_duration} seconds")
    logging.info(f"etl_duration: {etl_duration} seconds")
    
except Exception as e:
    print(f"ETL failed! Error: {e}")
    logging.exception(f"ETL failed! Error: {e}")