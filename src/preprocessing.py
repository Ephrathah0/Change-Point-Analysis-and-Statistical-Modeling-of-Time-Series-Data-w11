import pandas as pd

def set_time_index(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """
    Set date column as time index.
    """
    df = df.set_index(date_column)
    return df


def calculate_rolling_volatility(
    series: pd.Series,
    window: int
) -> pd.Series:
    """
    Calculate rolling standard deviation as volatility proxy.
    """
    return series.rolling(window=window).std()
