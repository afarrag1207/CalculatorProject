import unittest

from Calculator.Calculator import Calculator
from CSVReader.CSVReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add(self):
        test_data = CsvReader("Tests/Data/CSV_reader.csv").data
        for row in test_data:
            self.assertEqual(row['Value 1'], '580')


if __name__ == '__main__':
    unittest.main()

