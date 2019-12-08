from Statistics.Proportion import proportion
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division


def var_pop_prop(data):
    prob_poss = proportion(data)
    prob_imposs = subtraction(prob_poss, 1)
    result = multiplication(prob_imposs, prob_poss)
    vpp = division(result, len(data))
    return vpp
