# data_cleaning.py

import pandas as pd
import os

# Read the data
def read_data(path):
    files = [file for file in os.listdir(path) if not file.startswith('.')]

    all_months_data = pd.DataFrame()

    for file in files:
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join(path, file))
            all_months_data = pd.concat([all_months_data, df], ignore_index=True)

    return all_months_data

def data_info(df):
    print('Info:')
    print(df.info())
    print('')
    print('Null values: ')
    print(df.isnull().sum())

def clean_data(df):
    df = df.dropna(how='all')
    df = df[df['Order Date'].str[0:2] != 'Or']
    return df

def get_months(df):
    df['Month'] = df['Order Date'].str[0:2]
    df['Month'] = df['Month'].astype('int32')
    df.to_csv('../data/cleaned_data.csv', index=False)
    return df

def get_city(df):
    df['City'] = df['Purchase Address'].apply(lambda x: f"{x.split(',')[1]} ({x.split(',')[2].split(' ')[1]})" if len(x.split(',')) > 2 else None)
    return df