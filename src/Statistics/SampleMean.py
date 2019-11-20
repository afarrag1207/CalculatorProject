from Statistics.Mean import mean
from Statistics.sample import Sample


def samplemean(list):
    s=50
    r = Sample(list,s)
    c = mean(r)
    return c