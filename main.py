from etl.load import get_engine, load_dataframe
from etl.extract import extract_csv
from etl.transform import (
    clean_data,
    build_dim_customer,
    build_dim_product,
    build_dim_time,
    build_fact_sales
)


def run_etl():
    print("=== START ETL PROCESS ===")

    # =========================
    # EXTRACT
    # =========================
    print("\n[STEP] Extract")
    df_raw = extract_csv("data/raw/sales.csv")

    # =========================
    # TRANSFORM
    # =========================
    print("\n[STEP] Transform")
    df_clean = clean_data(df_raw)

    dim_customer = build_dim_customer(df_clean)
    dim_product = build_dim_product(df_clean)
    dim_time = build_dim_time(df_clean)
    fact_sales = build_fact_sales(df_clean)

    print("[TRANSFORM] Dimension & Fact tables created")

    # =========================
    # SUMMARY OUTPUT (OPTIONAL)
    # =========================
    print("\n[SUMMARY]")
    print(f"dim_customer rows : {len(dim_customer)}")
    print(f"dim_product rows  : {len(dim_product)}")
    print(f"dim_time rows     : {len(dim_time)}")
    print(f"fact_sales rows   : {len(fact_sales)}")

    print("\n=== ETL PROCESS FINISHED ===")

        # =========================
    # LOAD
    # =========================
    print("\n[STEP] Load")
    engine = get_engine()

    load_dataframe(dim_customer, "dim_customer", engine)
    load_dataframe(dim_product, "dim_product", engine)
    load_dataframe(dim_time, "dim_time", engine)
    load_dataframe(fact_sales, "fact_sales", engine)


    # Return results (optional, useful for testing or future use)
    return dim_customer, dim_product, dim_time, fact_sales


if __name__ == "__main__":
    run_etl()
