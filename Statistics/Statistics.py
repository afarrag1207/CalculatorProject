from Calculator.Calculator import Calculator
from CSVReader.CSVReader import CsvReader
from Statistics.Mean import mean
from Statistics.Mode import mod
from Statistics.Zscore import zscore
from Statistics.Vpp import var_pop_prop
from Statistics.Median import median
from Statistics.Proportion import proportion
from Statistics.ConfidenceInterval import confidenceinterval
from Statistics.PValue import pvalue
from Statistics.Vsp import vsp
from Statistics.Psd import psd


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):

        super().__init__()
        self.data = CsvReader(filepath)

    def mean(self, m):
        self.result = mean(m)
        return self.result

    def median(self, me):
        self.result = median(me)
        return self.result

    def mod(self, mo):
        self.result = mod(mo)
        return self.result

    def psd(self, po):
        self.result = psd(po)
        return self.result

    def z_score(self, a):
        self.result = zscore(a)

    def var_pop_proportion(self, a):
        self.result = var_pop_prop(a)
        return self.result

    def proportion(self, a):
        self.result = proportion(a)
        return self.result

    def conf_interval(self, a):
        self.result = confidenceinterval(a)
        return self.result

    def pvalue(self, a):
        return pvalue(a)

    def vsp(self, a):
        self.result = vsp(a)
        return self.result
