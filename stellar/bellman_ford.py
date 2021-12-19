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

    D, parents = bellman_ford(B, 0)
    print(f'Distances: {D}')
    print(f'Parents: {parents}')
