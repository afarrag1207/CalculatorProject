from Statistics.Mean import mean


def variance(data):
    n = len(data)
    varianceValue = 0
    meanData = mean(data)
    for i in data:
        varianceValue += (i - meanData) ** 2
    varianceValue /= n
    return varianceValue
