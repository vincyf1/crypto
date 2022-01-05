import numpy as np
import math


inf = math.inf


def bellman_ford(graph, source):
    n = len(graph)

    # Initialise distance vector
    d = np.full(n, inf)

    parents = {0: source}

    d[source] = 0
    d_old = d.copy()

    for key in range(1, n):
        print(f'vector {d}')
        for j in range(0, n):
            sum_d = d_old + graph[:, j].T
            min_val =  min(sum_d)
            if min_val < d[j]:
                d[j] = min_val
                parents[j] = np.argmin(sum_d)
        d_old = d.copy()
    return d, parents


if __name__ == '__main__':
    B = np.array([[inf, 8, inf, inf, 1],
                  [8, inf, 7, 3, 2],
                  [inf, 7, inf, 1, inf],
                  [inf, 3, 1, inf, 6],
                  [1, 2, inf, 6, inf]])

# XLM, ETH, BTC, BNB, USDT

    B1 = np.array(
        [[1, 0.0000725, 0.0000057, 0.000524, 0.2740],
         [inf, 1, 0.079063, inf, 3799.10],
         [inf, 12.65, 1, inf, 48005.71],
         [inf, 0.1375, 0.010869, 1, 521.4],
         [inf, inf, inf, inf, 1]]
    )

    D, parents = bellman_ford(B1, 0)
    print(f'Distances: {D}')
    print(f'Parents: {parents}')
