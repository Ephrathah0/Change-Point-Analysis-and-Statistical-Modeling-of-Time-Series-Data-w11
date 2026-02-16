import numpy as np
import pandas as pd

def calculate_rmse(
    actual: pd.Series,
    predicted: pd.Series
) -> float:
    return np.sqrt(np.mean((actual - predicted) ** 2))


def calculate_mape(
    actual: pd.Series,
    predicted: pd.Series
) -> float:
    return np.mean(np.abs((actual - predicted) / actual)) * 100
