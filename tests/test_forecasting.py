import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from src.forecasting import generate_forecast

def test_forecast_output_shape():
    series = pd.Series([50, 51, 52, 53, 54, 55])
    model = ARIMA(series, order=(1,1,0)).fit()

    forecast = generate_forecast(model, steps=3)

    assert forecast.shape[0] == 3
    assert "mean" in forecast.columns
