import unittest
from backend import Year
import pandas as pd


class TestYearMethods(unittest.TestCase):

    def testGetKW(self):
        y = Year("2050")
        y.population = 1000
        self.assertEqual(y.GetKW(), 8930000)

    def testSetPop(self):
        data = {'Year': ['2050', '2051', '2052'],
                'Medium series': ['1001', '1002', '1003']}
        y = Year('2050')
        y.population_dataset = pd.DataFrame(data)
        y.SetPop()
        self.assertEqual(y.population, 1001)
        y.year = 'asdassd'
        y.SetPop()
        self.assertEqual(y.population, False)
        y.year = '3000'
        y.SetPop()
        self.assertEqual(y.population, False)

    def testRun(self):
        y = Year('3000')
        self.assertEqual(y.run(), "Invalid Year entered")




