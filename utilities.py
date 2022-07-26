import random
import numpy as np

def monte_carlo_hits_numb(estimate_numb):
    hits = 0
    for _ in range(int(estimate_numb)):
        x, y = random.uniform(0,1), random.uniform(0,1)
        hits += x*x + y*y <= 1.0

    return hits

def numpy_monte_carlo_hits_numb(estimate_numb):
    np.random.seed()
    xs = np.random.uniform(0, 1, int(estimate_numb))
    ys = np.random.uniform(0, 1, int(estimate_numb))
    hits = np.sum((xs*xs + ys*ys) <= 1)
    return hits

