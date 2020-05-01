# %%
import pandas as pd
import numpy as np
import matplotlib as mp
import seaborn as sns
from matplotlib import pyplot as plt


# %%
fifa_data = pd.read_csv('fifa_data.csv')
fifa_data.head()


# %%
fifa_data = pd.read_csv('./fifa_data.csv')
fifa_data.head()


# %%
# Function to clean the monetary values, erase K,M and
def transform_money_to_number(string):
    last = len(string) - 1
    if 'K' in string:
        return float(string[1:last]) * 1000
    elif 'M' in string:
        return float(string[1:last]) * 1000000


# %%
fifa_data['Value'] = fifa_data['Value'].apply(transform_money_to_number)


# %%
fifa_data['Wage'].replace('[€K]', '', inplace=True, regex=True)
fifa_data.rename(index=str, columns={'Wage': 'WageInK'}, inplace=True)


# %%
fifa_data['WageInK'] = pd.to_numeric(fifa_data['WageInK'])


# %%
pd.set_option('display.max_columns', None)
clubs = fifa_data.groupby(by='Club').mean()
clubs.head()


# %%
# Remove irrelevant values from the clubs
clubs.drop(['ID', 'Jersey Number', 'Jumping', 'Unnamed: 0', 'LongPassing', 'LongShots', 'ShortPassing', 'Weak Foot', 'GKDiving',
            'GKKicking', 'GKHandling', 'GKPositioning', 'HeadingAccuracy', 'Curve', 'GKDiving', 'Stamina'], axis=1, inplace=True)


# %%
# Sorting clubs by overall rating
clubs_with_best_overall = clubs.sort_values(by='Overall', ascending=False)
clubs_with_best_overall.head()


# %%
# Plot the 5 best teams and changing the size of the plot to see difference
lm = sns.barplot(
    x=clubs_with_best_overall.index[:5], y=clubs_with_best_overall.Overall[:5], data=clubs_with_best_overall)
lm.set(ylim=(75, 83))
lm.set_title('Best teams')


# %%
