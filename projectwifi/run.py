"""
run.py — WiFi Multilateration: standalone integration script

Usage:
    python run.py          # live scan (falls back to demo if <3 known APs visible)
    python run.py --demo   # demo using sample CSV data only
"""

import sys
import os

# Allow imports from src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import pandas as pd
from wifi_scanner import scan_wifi
from rssi_model import rssi_to_distance
from multilateration import geo_multilateration
from visualization import plot_graph, create_map

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "wifi_data.csv")


def run_demo():
    """Run multilateration using sample CSV data (no live scan needed)."""
    print("=" * 50)
    print("DEMO MODE — using sample data from wifi_data.csv")
    print("=" * 50)

    df = pd.read_csv(DB_PATH)
    df["distance"] = df["rssi"].apply(rssi_to_distance)

    print("\nAccess Points:")
    for _, row in df.iterrows():
        print(f"  {row['ssid']:20s}  RSSI={row['rssi']:4d} dBm  →  dist={row['distance']:.2f} m")

    ap_lat_lon = list(zip(df["latitude"], df["longitude"]))
    distances = df["distance"].tolist()

    est_lat, est_lon = geo_multilateration(ap_lat_lon, distances)

    print(f"\nEstimated User Position:")
    print(f"  Latitude  : {est_lat:.6f}")
    print(f"  Longitude : {est_lon:.6f}")

    create_map(df, [est_lon, est_lat])
    plot_graph(df, [est_lon, est_lat])


def run_live():
    """Scan nearby WiFi, match against known AP database, run multilateration."""
    print("=" * 50)
    print("LIVE MODE — scanning WiFi networks...")
    print("=" * 50)

    scanned = scan_wifi()
    if not scanned:
        print("No WiFi networks found or scanner unavailable.")
        print("Falling back to demo mode.\n")
        run_demo()
        return

    print(f"\nFound {len(scanned)} networks nearby.")

    db = pd.read_csv(DB_PATH)

    # Match scanned SSIDs against known AP database
    matched = []
    for ap in scanned:
        row = db[db["ssid"] == ap["ssid"]]
        if not row.empty:
            row = row.iloc[0]
            distance = rssi_to_distance(ap["signalStrength"])
            matched.append({
                "ssid": row["ssid"],
                "latitude": row["latitude"],
                "longitude": row["longitude"],
                "rssi": ap["signalStrength"],
                "distance": distance,
            })

    print(f"Matched {len(matched)} known APs:")
    for m in matched:
        print(f"  {m['ssid']:20s}  RSSI={m['rssi']:4d} dBm  →  dist={m['distance']:.2f} m")

    if len(matched) < 3:
        print(f"\nNeed at least 3 known APs for multilateration (got {len(matched)}).")
        print("Falling back to demo mode.\n")
        run_demo()
        return

    matched_df = pd.DataFrame(matched)
    ap_lat_lon = list(zip(matched_df["latitude"], matched_df["longitude"]))
    distances = matched_df["distance"].tolist()

    est_lat, est_lon = geo_multilateration(ap_lat_lon, distances)

    print(f"\nEstimated User Position:")
    print(f"  Latitude  : {est_lat:.6f}")
    print(f"  Longitude : {est_lon:.6f}")

    create_map(matched_df, [est_lon, est_lat])
    plot_graph(matched_df, [est_lon, est_lat])


if __name__ == "__main__":
    if "--demo" in sys.argv:
        run_demo()
    else:
        run_live()
