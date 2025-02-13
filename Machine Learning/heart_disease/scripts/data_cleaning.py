# data_cleaning.py

import pandas as pd

def data_info(df):
    print('Info:')
    print(df.info())
    print('')
    print('Null values: ')
    print(df.isnull().sum())

def isDuplicate(data):
    print('Duplicate data: \n', data.duplicated().sum())