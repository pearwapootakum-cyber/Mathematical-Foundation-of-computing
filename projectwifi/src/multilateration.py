import numpy as np

def multilateration(ap_positions, distances):
    A = []
    b = []

    x0, y0 = ap_positions[0]
    d0 = distances[0]

    for i in range(1, len(ap_positions)):
        xi, yi = ap_positions[i]
        di = distances[i]

        A.append([2*(xi-x0), 2*(yi-y0)])
        b.append(d0**2 - di**2 - x0**2 + xi**2 - y0**2 + yi**2)

    A = np.array(A)
    b = np.array(b)

    position = np.linalg.lstsq(A, b, rcond=None)[0]
    return position
