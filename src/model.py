from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
from typing import Tuple

def fit_arima(
    series: pd.Series,
    order: Tuple[int, int, int]
):
    """
    Fit ARIMA model to time series.
    """
    model = ARIMA(series, order=order)
    fitted_model = model.fit()
    return fitted_model
