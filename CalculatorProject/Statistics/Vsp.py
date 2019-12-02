from Statistics.Proportion import proportion
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division
from Statistics.Sample import Getsample
import random


def vsp(data):
    random_data = random.randint(1, len(data))
    new_data = Getsample(data, random_data)
    prop = proportion(new_data)
    result1 = multiplication(prop, subtraction(prop, 1))
    y = subtraction(len(new_data), 1)
    x = division(result1, y)
    return x

