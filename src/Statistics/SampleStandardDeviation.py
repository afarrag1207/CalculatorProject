import random
from Calculator.addition import addition
from Calculator.division import division
from Calculator.Square import square
from Calculator.squareroot import squareroot
from Calculator.subtraction import subtraction
from Sample import sample
from Mean import mean
def ssd(data):
    total = 0
    sample =  random.randint(1, len(data))
    new_sample = sample(data, sample)
    new_mean = mean(new_sample)
    for numb in new_sample:
        result = subtraction(numb, new_mean)
        sq = square(result)
        total = addition(total, sq)
    n = len(new_sample)
    d = division(subtraction(1, n), total)
    samp_sd = squareroot(d)
    return samp_sd