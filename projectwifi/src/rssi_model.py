import numpy as np

def rssi_to_distance(rssi, A=-40, n=2):
   
    return 10 ** ((A - rssi) / (10 * n))

#logarithm path loss model