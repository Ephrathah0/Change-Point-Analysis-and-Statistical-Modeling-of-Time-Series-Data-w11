import pandas as pd
from typing import Tuple

def generate_forecast(
    fitted_model,
    steps: int
) -> pd.DataFrame:
    """
    Generate forecast with confidence intervals.
    """
    forecast_result = fitted_model.get_forecast(steps=steps)
    forecast_df = forecast_result.summary_frame()

    return forecast_df[["mean", "mean_ci_lower", "mean_ci_upper"]]
