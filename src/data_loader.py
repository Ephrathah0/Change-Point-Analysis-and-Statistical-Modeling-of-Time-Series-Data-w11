import pandas as pd
from pathlib import Path

def load_data(path: Path, date_column: str) -> pd.DataFrame:
    """
    Load Brent oil price dataset.
    """
    df = pd.read_csv(path)
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values(date_column)
    return df
