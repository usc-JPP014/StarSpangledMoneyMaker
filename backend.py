import pandas as pd
import numpy as np


class Year:

    def __init__(self, y):
        self.year = y
        self.population = None
        self.population_dataset = pd.read_csv("Projected population, Australia.csv", header=1)
        self.powerStation_dataset = None
        self.population_dataset = self.population_dataset.rename(columns={'Unnamed: 0': "Year"})
        self.powerStation_dataset = pd.read_csv("MajorPowerStations_v2.csv", header=0, index_col=0)
        self.plant_types = self.powerStation_dataset['PRIMARYFUELTYPE'].unique()
        self.plant_types = np.delete(self.plant_types, np.where(self.plant_types == ["Diesel"]))

    def GetNumberOfPowerplants(self):
        string = ''
        for plant in self.plant_types:
            arr = []

            for row in self.powerStation_dataset.iterrows():
                if row[1][8] == plant:
                    arr.append(int(row[1][10]))

            average = ((round(round(sum(arr)) / len(arr))) * 1000) * 8765
            string = string + "<br/>     {number} {type} plants".format(number=round(self.GetKW() / average),
                                                                        type=plant)
        return string

    def SetPop(self):
        if not self.year.isnumeric() or 2016 < int(self.year) > 2066:
            self.population = False
        else:
            yearIndex = self.population_dataset[self.population_dataset['Year'] == self.year].index.values
            pop = self.population_dataset["Medium series"][yearIndex].tolist()[0]
            pop = pop.replace(',', '')
            self.population = int(pop)

    def GetKW(self):
        return 8930 * self.population

    def run(self):
        self.SetPop()
        if not self.population:
            return "Invalid Year entered"
        kilowatt = self.GetKW()

        return "By {year} Australia will have a projected population of {pop}, to support this population Australia " \
               "will have to produce at least {kw} Billion Kwh per year. <br/>This is equivalent to:".format(
                year=self.year, pop=self.population, kw=kilowatt / 1000000000) + self.GetNumberOfPowerplants()
