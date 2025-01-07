import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def join_data(files):
    
    dfs = []

    for file in files:
        if file.endswith('.xlsx'):
            year = file.split('.')[0]
            data = pd.read_excel('../data/' + file, sheet_name='By-HS6Product')
            data = data[['Reporter', 'Quantity']]
            data = data.fillna(0)
            data['Quantity'] = data['Quantity'].astype('float').apply(lambda x: x / 1000)
            data['Quantity'] = data['Quantity'].apply(lambda x: '%.0f' % x)
            data = data.replace('0', np.nan)
            data = data.rename(columns={'Reporter': 'Countries', 'Quantity': year})
            dfs.append(data)  

    final_df = dfs[0]
    for df in dfs[1:]:
            final_df = final_df.merge(df, on='Countries', how='outer')

    return final_df

def clean_data(data, countries):

    data = data[data['Countries'].isin(countries)]

    df = data.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
    df = df.apply(fill_missing_with_regression, axis=1)
    data = pd.merge(data.iloc[:, :1], df.astype(int), left_index=True, right_index=True)

    return data

def fill_missing_with_regression(row):
    # Identify non-NaN values
    not_nan = row.dropna()
    
    if len(not_nan) > 1:  # If there are enough non-NaN values to fit a model
        years = np.array([int(year) for year in not_nan.index]).reshape(-1, 1)
        values = not_nan.values
        
        # Fit the linear regression model
        model = LinearRegression()
        model.fit(years, values)
        
        # Predict missing values
        for year in row.index:
            if pd.isna(row[year]):
                predicted_value = model.predict([[int(year)]])
                row[year] = predicted_value[0]
    return row