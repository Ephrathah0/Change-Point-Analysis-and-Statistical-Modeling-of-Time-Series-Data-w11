from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load data
prices_df = pd.read_csv("data/brent_oil_prices.csv")
events_df = pd.read_csv("data/oil_market_events.csv")

# Convert Date columns to datetime
prices_df["Date"] = pd.to_datetime(prices_df["Date"], errors="coerce")
events_df["Start Date"] = pd.to_datetime(events_df["Start Date"], errors="coerce")

# API endpoint: all prices
@app.route("/api/prices", methods=["GET"])
def get_prices():
    data = prices_df.to_dict(orient="records")
    return jsonify(data)

# API endpoint: all events
@app.route("/api/events", methods=["GET"])
def get_events():
    data = events_df.to_dict(orient="records")
    return jsonify(data)

# API endpoint: change point info
@app.route("/api/change_point", methods=["GET"])
def get_change_point():
    # Hardcode latest change point from your model
    change_point = {
        "date": "2020-03-06",  # Replace with your detected date
        "mean_before": 0.0005,  # Replace with posterior mean
        "mean_after": -0.0021,  # Replace with posterior mean
        "volatility_before": 0.015,  # Replace with posterior sigma1
        "volatility_after": 0.032  # Replace with posterior sigma2
    }
    return jsonify(change_point)

if __name__ == "__main__":
    app.run(debug=True)
