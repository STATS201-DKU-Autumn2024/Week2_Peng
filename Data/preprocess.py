import ipdb
# ipdb.set_trace()
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns



data = pd.read_csv('wind_gen_cf_2020.csv', parse_dates=['datetime'], index_col='datetime')


def visualize():
    data = pd.read_csv("eia_wind_configs.csv")

    sns.set(style="whitegrid")


    plt.figure(figsize=(12, 8))
    scatter = sns.scatterplot(
        x="lon", y="lat", data=data, hue="state", palette="tab20", s=50, legend="full"
    )

    plt.title("Wind Plant Locations by State")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(title="State", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(True)
    plt.tight_layout()

    plt.show()
    state_counts = data['state'].value_counts()
    top_5_states = state_counts.head(5)
    top_5_states




def pre():

    print(data.head())
    print(data.info())
    missing_values = data.isnull().sum()
    print("Missing values:", missing_values[missing_values > 0])

def feature():
    data['hour'] = data.index.hour
    data['day_of_week'] = data.index.dayofweek
    data['month'] = data.index.month
    data['day_of_year'] = data.index.dayofyear
    data['week_of_year'] = data.index.isocalendar().week
    print(data.head())


if __name__ == '__main__':
    # pre()
    # feature()
    visualize()