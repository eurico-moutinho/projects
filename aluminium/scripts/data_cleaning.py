import pandas as pd
import numpy as np

def join_data(files):
    
    dfs = []

    for file in files:
        if file.endswith('.xlsx'):
            year = file.split('.')[0]
            data = pd.read_excel('../data/' + file, sheet_name='By-HS6Product')
            data = data[['Reporter', 'Quantity']]
            data = data.fillna(0)
            data['Quantity'] = data['Quantity'].astype('float').apply(lambda x: '%.0f' % x)
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
    df.interpolate(method='linear', axis=1, inplace=True)
    df.fillna(329708000, inplace=True)
    data = pd.merge(data.iloc[:, :1], df.astype(int), left_index=True, right_index=True)

    return data