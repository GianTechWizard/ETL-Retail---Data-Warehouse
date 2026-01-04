import pandas as pd


# =========================
# CLEANING DATA
# =========================
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic data cleaning and standardization.
    """
    df = df.copy()

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Convert date columns
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Convert sales to numeric
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

    # Drop rows with critical null values
    df = df.dropna(subset=["order_date", "customer_id", "product_id", "sales"])

    return df

# =========================
# DIMENSION TABLES
# =========================
def build_dim_customer(df: pd.DataFrame) -> pd.DataFrame:
    dim_customer = (
        df[[
            "customer_id",
            "customer_name",
            "segment",
            "region",
            "city",
            "state",
            "postal_code"
        ]]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    return dim_customer


def build_dim_product(df: pd.DataFrame) -> pd.DataFrame:
    dim_product = (
        df[[
            "product_id",
            "product_name",
            "category",
            "sub_category"
        ]]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    return dim_product


def build_dim_time(df: pd.DataFrame) -> pd.DataFrame:
    dim_time = (
        df[["order_date"]]
        .drop_duplicates()
        .rename(columns={"order_date": "full_date"})
    )

    dim_time["date_id"] = dim_time["full_date"].dt.strftime("%Y%m%d").astype(int)
    dim_time["day"] = dim_time["full_date"].dt.day
    dim_time["month"] = dim_time["full_date"].dt.month
    dim_time["year"] = dim_time["full_date"].dt.year

    dim_time = dim_time.reset_index(drop=True)
    return dim_time

# =========================
# FACT TABLE
# =========================
def build_fact_sales(df: pd.DataFrame) -> pd.DataFrame:
    fact_sales = df.copy()

    fact_sales["date_id"] = fact_sales["order_date"].dt.strftime("%Y%m%d").astype(int)

    fact_sales = fact_sales[[
        "order_id",
        "date_id",
        "customer_id",
        "product_id",
        "sales"
    ]].rename(columns={"sales": "sales_amount"})

    fact_sales = fact_sales.reset_index(drop=True)
    fact_sales.index += 1
    fact_sales.insert(0, "sales_id", fact_sales.index)

    return fact_sales
