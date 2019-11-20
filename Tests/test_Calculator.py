import unittest

from Calculator.Calculator import Calculator

from CSVReader.CSVReader import CsvReader

from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_properties(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition_calculator(self):
        test_Data = CsvReader("/src/Tests/Data/UnitTestAddition.csv").data
        pprint(test_Data)
        for row in test_Data:
            self.assertEqual(self.calculator.add(row["Value 1"], row["Value 2"]), float(row["Result"]))
            self.assertEqual(self.calculator.result, float(row["Result"]))


    def test_subtraction_calculator(self):
        test_Data = CsvReader("/src/Tests/Data/UnitTestSubtraction.csv").data
        pprint(test_Data)
        for row in test_Data:
            self.assertEqual(self.calculator.subtract(row["Value 1"], row["Value 2"]), float(row["Result"]))
            self.assertEqual(self.calculator.result, float(row["Result"]))


    def test_multiplication_calculator(self):
        test_Data = CsvReader("/src/Tests/Data/UnitTestMultiplication.csv").data
        pprint(test_Data)
        for row in test_Data:
            self.assertEqual(self.calculator.multiply(row["Value 1"], row["Value 2"]), float(row["Result"]))
            self.assertEqual(self.calculator.result, float(row["Result"]))


    def test_division_calculator(self):
        test_Data = CsvReader("/src/Tests/Data/UnitTestDivision.csv").data
        pprint(test_Data)
        for row in test_Data:
            self.assertEqual(self.calculator.divide(row["Value 1"], row["Value 2"]), float(row["Result"]))
            self.assertEqual(self.calculator.result, float(row["Result"]))


    def test_square_calculator(self):
        test_Data = CsvReader("/src/Tests/Data/UnitTestSquare.csv").data
        pprint(test_Data)
        for row in test_Data:
            self.assertEqual(self.calculator.squared(row["Value 1"]), float(row["Result"]))
            self.assertEqual(self.calculator.result, float(row["Result"]))

    def test_squareroot_calculator(self):
        test_Data = CsvReader("/src/Tests/Data/UnitTestSquareRoot.csv").data
        pprint(test_Data)
        for row in test_Data:
            self.assertEqual(self.calculator.sqrt(row["Value 1"]), float(row["Result"]))
            self.assertEqual(self.calculator.result, float(row["Result"]))


if __name__ == '__main__':
    unittest.main()
