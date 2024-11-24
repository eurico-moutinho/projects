import pandas as pd

def info_data(data):
    print(data.info())

def isNull(data):
    print('Null data: \n', data.isnull().sum())

def isDuplicate(data):
    print('Duplicate data: \n', data.duplicated().sum())

def save_data(data, path):
    data.to_csv(path, index=False)

def date_to_months_and_year(data):
    data['Date'] = pd.to_datetime(data['Date'])
    data['Month'] = data['Date'].dt.month_name().str.slice(stop=3)
    data['Year'] = data['Date'].dt.year
    data = data.drop('Date', axis=1)
    return data