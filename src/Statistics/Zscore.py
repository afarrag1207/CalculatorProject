from Calculator.division import division
from Calculator.subtraction import subtraction
from Statistics.Mean import mean
from Statistics.Psd import psd


def zscore(numbers):
    row_value = 484
    sd = psd(numbers)
    m = mean(numbers)
    result = subtraction(m, row_value)
    return division(sd, result)
