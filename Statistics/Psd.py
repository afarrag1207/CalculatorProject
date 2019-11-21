from Calculator.addition import addition
from Calculator.division import division
from Calculator.Square import square
from Calculator.Squareroot import squareroot
from Calculator.subtraction import subtraction
from Statistics.Mean import mean


def psd(numbers):
    num_values = len(numbers)

    result = mean(numbers)
    total = 0
    for numb in numbers:
        result2 = subtraction(numb, result)
        sq = square(result2)
        total = addition(total, sq)
        result3 = division(num_values, total)
    return squareroot(result3)