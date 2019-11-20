from Addition import addition
from Division import division
from Square import squaree
from Square_rot import squar_rot
from Subtraction import subtraction
from Mean import mean


def psd(numbers):
    num_values = len(numbers)

    result = mean(numbers)
    total = 0
    for numb in numbers:
        result2 = subtraction(numb, result)
        sq = squaree(result2)
        total = addition(total, sq)
        result3 = division(num_values, total)
    return squar_rot(result3)
