
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import pandas as pd
from flask import Flask, jsonify, render_template

from wifi_scanner import scan_wifi
from rssi_model import rssi_to_distance
from multilateration import geo_multilateration

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "..", "templates")
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "wifi_data.csv")

app = Flask(__name__, template_folder=TEMPLATES_DIR)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/scan")
def scan():
    try:
        scanned = scan_wifi()
    except Exception as e:
        return jsonify({"error": f"WiFi scan failed: {e}"}), 500

    if not scanned:
        return jsonify({"error": "No WiFi networks found. Try /demo instead."}), 200

    db = pd.read_csv(DB_PATH)
    matched = []

    for ap in scanned:
        row = db[db["ssid"] == ap.get("ssid", "")]
        if not row.empty:
            row = row.iloc[0]
            distance = rssi_to_distance(ap["signalStrength"])
            matched.append({
                "ssid": str(row["ssid"]),
                "latitude": float(row["latitude"]),
                "longitude": float(row["longitude"]),
                "rssi": int(ap["signalStrength"]),
                "distance": round(float(distance), 2),
            })

    if len(matched) < 3:
        return jsonify({
            "error": f"Only {len(matched)} known AP(s) visible — need at least 3 for multilateration.",
            "scanned_count": len(scanned),
            "matched": matched,
        }), 200

    ap_lat_lon = [(ap["latitude"], ap["longitude"]) for ap in matched]
    distances = [ap["distance"] for ap in matched]
    est_lat, est_lon = geo_multilateration(ap_lat_lon, distances)

    return jsonify({
        "mode": "live",
        "position": {
            "latitude": round(est_lat, 6),
            "longitude": round(est_lon, 6),
        },
        "access_points": matched,
    })


@app.route("/demo")
def demo():
    
    df = pd.read_csv(DB_PATH)
    df["distance"] = df["rssi"].apply(rssi_to_distance)

    ap_lat_lon = list(zip(df["latitude"], df["longitude"]))
    distances = df["distance"].tolist()
    est_lat, est_lon = geo_multilateration(ap_lat_lon, distances)

    access_points = [
        {
            "ssid": str(row["ssid"]),
            "latitude": float(row["latitude"]),
            "longitude": float(row["longitude"]),
            "rssi": int(row["rssi"]),
            "distance": round(float(row["distance"]), 2),
        }
        for _, row in df.iterrows()
    ]

    return jsonify({
        "mode": "demo",
        "position": {
            "latitude": round(est_lat, 6),
            "longitude": round(est_lon, 6),
        },
        "access_points": access_points,
    })


if __name__ == "__main__":
    app.run(debug=True)
