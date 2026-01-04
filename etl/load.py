from sqlalchemy import create_engine
from config.db_config import DB_CONFIG


def get_engine():
    """
    Create SQLAlchemy engine for PostgreSQL.
    """
    db_url = (
        f"postgresql+psycopg2://{DB_CONFIG['user']}:"
        f"{DB_CONFIG['password']}@{DB_CONFIG['host']}:"
        f"{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )
    engine = create_engine(db_url)
    return engine


def load_dataframe(df, table_name: str, engine):
    """
    Load DataFrame into PostgreSQL table.
    """
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )
    print(f"[LOAD] Table '{table_name}' loaded successfully ({len(df)} rows)")
