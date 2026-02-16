from config import Config
from data_loader import load_data
from preprocessing import set_time_index, calculate_rolling_volatility
from model import fit_arima
from forecasting import generate_forecast

def main():
    config = Config()

    df = load_data(config.data_path, config.date_column)
    df = set_time_index(df, config.date_column)

    series = df[config.price_column]

    fitted_model = fit_arima(
        series,
        (config.p, config.d, config.q)
    )

    forecast = generate_forecast(
        fitted_model,
        config.forecast_horizon
    )

    volatility = calculate_rolling_volatility(
        series,
        config.rolling_window
    )

    print(forecast.tail())
    print(volatility.tail())


if __name__ == "__main__":
    main()
