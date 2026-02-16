import pandas as pd
from src.preprocessing import set_time_index

def test_set_time_index():
    df = pd.DataFrame({
        "Date": pd.date_range("2020-01-01", periods=3),
        "Price": [50, 51, 52]
    })

    df_indexed = set_time_index(df, "Date")

    assert df_indexed.index.name == "Date"
