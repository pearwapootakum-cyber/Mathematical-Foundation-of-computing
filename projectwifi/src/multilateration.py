import numpy as np
import math

#It takes the known coordinates of WiFi access points and their estimated distances from the user
def multilateration(ap_positions, distances):
   
    A = []
    b = []

    x0, y0 = ap_positions[0]
    d0 = distances[0]

    for i in range(1, len(ap_positions)):
        xi, yi = ap_positions[i]
        di = distances[i]
        A.append([2 * (xi - x0), 2 * (yi - y0)])
        b.append(d0**2 - di**2 - x0**2 + xi**2 - y0**2 + yi**2)

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    position, *_ = np.linalg.lstsq(A, b, rcond=None)
    return position



_METERS_PER_DEG_LAT = 111_320.0          

def _lon_scale(lat_deg):
    return _METERS_PER_DEG_LAT * math.cos(math.radians(lat_deg))


def geo_multilateration(ap_lat_lon, distances):
   
    if len(ap_lat_lon) < 2:
        raise ValueError("Need at least 2 access points.")

    # Reference origin: first AP  
    # Least squares is used to minimize errors caused by noise in RSSI measurements.
    lat0, lon0 = ap_lat_lon[0]
    scale_lon = _lon_scale(lat0)

    local_positions = [
        ((lon - lon0) * scale_lon, (lat - lat0) * _METERS_PER_DEG_LAT)
        for lat, lon in ap_lat_lon
    ]

    pos_m = multilateration(local_positions, distances)

    est_lat = lat0 + pos_m[1] / _METERS_PER_DEG_LAT
    est_lon = lon0 + pos_m[0] / scale_lon

    return float(est_lat), float(est_lon)
