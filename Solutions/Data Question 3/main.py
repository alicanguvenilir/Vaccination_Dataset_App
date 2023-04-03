import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\country_vaccination_stats.csv')

sum_of_vaccinations = df[df['date'] == '1/6/2021']['daily_vaccinations'].sum()

print(sum_of_vaccinations)
