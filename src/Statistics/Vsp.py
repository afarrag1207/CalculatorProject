from Statistics.Proportion import proportion
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Square_rot import squar_rot
from Statistics.Getsample import getSample
import random


def var_samp_prop(data):
    random_data = random.randint(1,len(data))
    new_data = getSample(data, random_data)
    prop = proportion(new_data)
    result1 = multiplication(prop, subtraction(prop, 1))
    y = subtraction(len(new_data), 1)
    x = division(result1, y)
    return x

