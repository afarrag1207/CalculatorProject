import random


def Getsample(data, sample_size):
    random_values = random.choices(data, k=sample_size - 1)
    return random_values
