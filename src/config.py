from dataclasses import dataclass
from pathlib import Path

@dataclass
class Config:
    data_path: Path = Path("data/raw/brent.csv")
    date_column: str = "Date"
    price_column: str = "Price"

    # ARIMA order
    p: int = 1
    d: int = 1
    q: int = 1

    forecast_horizon: int = 30
    rolling_window: int = 30
