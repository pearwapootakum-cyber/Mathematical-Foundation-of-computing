import subprocess
import re

AIRPORT_PATH = "/Applications/Utilities/AirPort Utility.app/Contents/Resources/airport"

def scan_wifi():
    result = subprocess.run(
        [AIRPORT_PATH, "-s"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.split("\n")[1:]
    wifi_list = []

    for line in lines:
        parts = re.split(r"\s{2,}", line.strip())
        if len(parts) >= 3:
            wifi_list.append({
                "macAddress": parts[1],
                "signalStrength": int(parts[2])
            })

    return wifi_list
