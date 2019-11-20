import unittest

from Statistics import Statistics
from pprint import pprint
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

     def test_mean(self):
         test_data = CsvReader("Tests/Data/datapoints.csv")
         answers = CsvReader("Tests/Data/answers.csv").data
         values = fetchRawdata(test_data, 'value')
         for column in answers:
             self.assertEqual(self.statistics.mean(values), float((column['mean'])))
        # self.assertEqual(self.statistics.mean(), 4.0)

    def test_median(self):
        test_data = CsvReader("Tests/Data/datapoints.csv")
        answers = CsvReader("Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.median(values), float((column['median'])))
    
    def test_mode(self):
        test_data = CsvReader("Tests/Data/datapoints.csv")
        answers = CsvReader("Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.mod(values), float((column['mode'])))

    def test_psd(self):
        test_data = CsvReader("Tests/Data/datapoints.csv")
        answers = CsvReader("Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        for column in answers:
            self.assertEqual(round(self.statistics.psd(values), 4), float((column['PSD'])))

     def test_variance_population_proportion(self):
        test_data = CsvReader("Tests/Data/datapoints.csv")
        answers = CsvReader("Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.var_pop_proportion(values), float((column['VPP'])))
    #        self.assertNotEqual(self.statistics.var_pop_proportion(values), float((column['var_pop_prop'])) - 2,
    #                            "WrongResult")

    

    #def test_zscore(self):
    #    test_data = CsvReader("Tests/Data/datapoints.csv")
     #   answers = CsvReader("Tests/Data/answers.csv").data
     #   values = fetchRawdata(test_data, 'value')
        # pprint(values)
     #   for column in answers:
     #       self.assertEqual(self.statistics.z_score(values), (column['zscore']))


        
if __name__ == '__main__':
    unittest.main()
