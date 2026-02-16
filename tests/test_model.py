import pandas as pd
from src.model import fit_arima

def test_arima_fits():
    series = pd.Series([50, 51, 52, 53, 54, 55])
    model = fit_arima(series, (1, 1, 0))

    assert model is not None
