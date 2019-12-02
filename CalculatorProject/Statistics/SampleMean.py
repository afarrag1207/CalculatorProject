from Statistics.Mean import mean
from Statistics.Sample import Getsample


def samplemean(list):
    s=50
    r = Getsample(list,s)
    c = mean(r)
    return c