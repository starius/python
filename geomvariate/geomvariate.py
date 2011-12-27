import random

def geomvariate(m):
    """
    m = 1 / p - 1
    p - probability of success
    x = number of non-success probes
    """
    p = 1.0 / (m + 1)
    r = 0
    while random.random() >= p:
        r += 1
    return r
