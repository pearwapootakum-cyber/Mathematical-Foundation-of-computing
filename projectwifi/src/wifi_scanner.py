import subprocess
import re
import os

_AIRPORT_CANDIDATES = [
    "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport",
    "/usr/sbin/airport",
]

def _find_airport():
    for path in _AIRPORT_CANDIDATES:
        if os.path.isfile(path):
            return path
    return None

def scan_wifi():
   
    airport = _find_airport()
    if not airport:
        print("[wifi_scanner] airport utility not found on this system.")
        return []

    try:
        result = subprocess.run(
            [airport, "-s"],
            capture_output=True,
            text=True,
            timeout=10
        )
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        print(f"[wifi_scanner] Scan failed: {e}")
        return []

    wifi_list = []
 
    for line in result.stdout.split("\n")[1:]:
        line = line.strip()
        if not line:
            continue
        parts = re.split(r"\s{2,}", line)
        if len(parts) < 3:
            continue
        try:
            wifi_list.append({
                "ssid": parts[0],
                "macAddress": parts[1],
                "signalStrength": int(parts[2])
            })
        except (ValueError, IndexError):
            continue

    return wifi_list
