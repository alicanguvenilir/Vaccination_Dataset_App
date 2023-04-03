#encoding:utf-8

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\country_vaccination_stats.csv')

all_countries = df['country'].drop_duplicates()


for i in range(len(df)):
    try:
        specific_country = all_countries[i]
        minimum_value = df[df['country'] == specific_country]['daily_vaccinations'].min()

    except:
        pass

    if str(df.values[i][2]) == "nan":
        if len(df[df['country'] == specific_country]['daily_vaccinations']) != 1:
            df.loc[i, 'daily_vaccinations'] = minimum_value
        elif len(df[df['country'] == specific_country]['daily_vaccinations']) == 1:
            df.loc[i, 'daily_vaccinations'] = '0'

df.to_csv(r'C:\Users\User\Desktop\country_vaccination_stats(1).csv')







