import math

def pvalue(a, b, c, d):

    p = float(a / b)
    p1 = float(c)
    n = float(b)
    f = float(p - p1)
    y = float(p1 * (1 - p1))
    y2 = float(y)
    y3 = float(y2 / n)
    z = float(f / math.sqrt(y3))
    norm = d
    pval = 1 - float(norm)

    return pval

