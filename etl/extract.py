import pandas as pd


def extract_csv(file_path: str) -> pd.DataFrame:
    """
    Extract data from CSV file.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Raw data as DataFrame.
    """
    try:
        df = pd.read_csv(file_path, sep=";")
        print(f"[EXTRACT] Successfully extracted data from {file_path}")
        print(f"[EXTRACT] Number of rows: {df.shape[0]}")
        print(f"[EXTRACT] Number of columns: {df.shape[1]}")
        return df

    except Exception as e:
        print("[EXTRACT] Error occurred while extracting data")
        raise e
