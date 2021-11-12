import pandas as pd
import numpy as np
population_dataset = pd.read_csv("Projected population, Australia.csv", header=1)
population_dataset = population_dataset.rename(columns={'Unnamed: 0': "Year"})

powerStation_dataset = pd.read_csv("MajorPowerStations_v2.csv", header=0, index_col=0)

plant_types = powerStation_dataset['PRIMARYFUELTYPE'].unique()
plant_types = np.delete(plant_types, np.where(plant_types == ["Diesel"]))

def printNumPowerplants(total_kilowatt):
    for plant in plant_types:
        arr = []

        for row in powerStation_dataset.iterrows():
            if row[1][8] == plant:
                arr.append(row[1][10])

        average = ((round(round(sum(arr)) / len(arr))) * 1000) * 8765
        print("     %d %s plants" % (total_kilowatt / average, plant))


class Year:

    def __init__(self, y):
        self.year = y
        self.population = None

    def CalculatePop(self):
        yearIndex = population_dataset[population_dataset['Year'] == self.year].index.values
        pop = population_dataset["Medium series"][yearIndex].tolist()[0]
        pop = pop.replace(',', '')
        self.population = int(pop)

    def CalculateKW(self):
        return 8930 * self.population

    def run(self):
        self.CalculatePop()
        kilowatt = self.CalculateKW()

        print(
            "By %s Australia will have a projected population of %d, to support this population Australia will have to "
            "produce at least %d Billion Kwh per year." % (self.year, self.population, kilowatt / 1000000000))
        print("This is equivalent to:")
        printNumPowerplants(kilowatt)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    year = Year('2050')
    year.run()
