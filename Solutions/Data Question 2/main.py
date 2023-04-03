import heapq
from statistics import median

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\country_vaccination_stats.csv')

all_countries = df['country'].drop_duplicates()
all_median_values = []


for i in range(len(df)):
    try:
        specific_country = all_countries[i]
        median_value = df[df['country'] == specific_country]['daily_vaccinations'].median()
        all_median_values.append(median_value)

    except:
        pass


print(heapq.nlargest(3, zip(all_median_values)))