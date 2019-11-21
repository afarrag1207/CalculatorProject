from Calculator.division import division
from Calculator.subtraction import subtraction
from Statistics.Mean import mean
from Statistics.Psd import psd


def zscore(numbers):
    row_value = 151
    sd = psd(numbers)
    m = mean(numbers)
    result = subtraction(row_value, m)
    z_score = division(result, sd)
    print(z_score)
    return z_score

