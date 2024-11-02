import ipdb
# ipdb.set_trace()
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns



data = pd.read_csv('Week2_Peng/Data/wind_gen_cf_2020.csv', parse_dates=['datetime'], index_col='datetime')


def visualize():
    data = pd.read_csv("Week2_Peng/Data/eia_wind_configs.csv")

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
    data['hour'] = data.index.hour
    data['day_of_week'] = data.index.dayofweek
    data['month'] = data.index.month
    data['day_of_year'] = data.index.dayofyear
    data['week_of_year'] = data.index.isocalendar().week
    print(data.head())
    # # Add lag features
    # for lag in [1, 3, 24]:
    #     data[f'lag_{lag}_hour'] = data['wind_plant_MW'].shift(lag)
    # # Add rolling statistics features
    # data['rolling_mean_24h'] = data['wind_plant_MW'].rolling(window=24).mean()
    # data['rolling_std_24h'] = data['wind_plant_MW'].rolling(window=24).std()
    # # 7-day rolling mean and standard deviation
    # data['rolling_mean_7d'] = data['wind_plant_MW'].rolling(window=24*7).mean()
    # data['rolling_std_7d'] = data['wind_plant_MW'].rolling(window=24*7).std()



if __name__ == '__main__':
    # pre()

    visualize()