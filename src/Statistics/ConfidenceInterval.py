from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.division import division
from Calculator.multiplication import multiplication
from Calculator.Squareroot import squareroot
from Statistics.Mean import mean
from Statistics.populationStandardDeviation import Psd


def confidence_interval(data):
    x = mean(data)
    dev = Psd(data)
    z = 1.96  # for 95% confidence

    standard_error = division(dev, squareroot(len(data)))
    conf_upper_level = round(addition(x, multiplication(z, standard_error)), 2)
    conf_lower_level = round(subtraction(multiplication(z, standard_error), x), 2)
    return conf_upper_level, conf_lower_level

