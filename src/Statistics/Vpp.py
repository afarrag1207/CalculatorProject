from Statistics.Proportion import proportion
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division


def var_pop_prop(data):
    prob_poss = proportion(data)
    prob_imposs = subtraction(prob_poss, 1)
    result = multiplication(prob_imposs, prob_poss)
    vpp = division(result, len(data))
    return vpp
