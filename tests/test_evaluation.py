import pandas as pd
from pathlib import Path
from src.data_loader import load_data

def test_load_data_returns_dataframe(tmp_path):
    test_file = tmp_path / "test.csv"
    df = pd.DataFrame({
        "Date": ["2020-01-01", "2020-01-02"],
        "Price": [50, 51]
    })
    df.to_csv(test_file, index=False)

    loaded_df = load_data(test_file, "Date")

    assert isinstance(loaded_df, pd.DataFrame)
    assert "Date" in loaded_df.columns
