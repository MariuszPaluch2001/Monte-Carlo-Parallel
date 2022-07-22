import random

def monte_carlo_hits_numb(estimate_numb):
    hits = 0
    for _ in range(int(estimate_numb)):
        x, y = random.uniform(0,1), random.uniform(0,1)
        hits += x*x + y*y <= 1.0

    return hits
