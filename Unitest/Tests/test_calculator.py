

from Unitest.Aplication.calculator import Calculator


class Test_calculator():
    def setup(self):
        self.calculator = Calculator()
    def teardown(self):
        print('Am terminat de executat instructiunile')


    def test_adunare(self):
        self.calculator.adunare(5,5)


