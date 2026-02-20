import numpy as np

def rssi_to_distance(rssi, A=-40, n=2):
    """
    Convert RSSI to distance using path loss model
    """
    return 10 ** ((A - rssi) / (10 * n))
