
import pandas as pd

#
# Dateien einlesen
#
countries = pd.read_csv("countries.csv", index_col=0)

fertility = pd.read_csv("gapminder_total_fertility.csv", index_col=0)

pop = pd.read_excel('gapminder_population.xlsx', index_col=0)

income = pd.read_json("gapminder_gdp_per_capita.json")

#
# Vereinigen
#
pop2 = pop.stack()
pop2.name = 'population'

fert2 = fertility.stack()
fert2.name = 'fertility'

# compare with
pop.transpose().stack()

pop.merge(fertility, 'outer', left_index=True, right_index=True)


countries.to_clipboard(index=False)

