# eda.py

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

def get_total_sales(df):
    df['Sales'] = df['Quantity Ordered'].astype('int') * df['Price Each'].astype('float')
    print(df.loc[:,['Month', 'Quantity Ordered', 'Sales']].groupby(['Month']).sum())
    return df

def plot_sales_per_month(df):
    months = range(1,13)
    plt.bar(months, df.groupby(['Month']).sum()['Sales'])
    plt.xticks(months, [pd.to_datetime(f'2020-{month}-01').strftime('%b') for month in months], rotation=45)
    plt.xlabel('Month')
    plt.ylabel('Sales in USD ($)')
    plt.show()

def plot_sales_per_city(df):
    cities = [city for city, df in df.groupby('City')]
    plt.bar(cities, df.groupby(['City']).sum()['Sales'])
    plt.xticks(cities, rotation=45, size=8, ha='right')
    plt.xlabel('City')
    plt.ylabel('Sales in USD ($)')
    plt.show()

def plot_sales_time(df):
    df['Hour'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y %H:%M').dt.hour
    hours = [hour for hour, df in df.groupby('Hour')]
    plt.plot(hours, df.groupby(['Hour']).sum()['Sales'])
    plt.ticklabel_format(style='plain')
    plt.xticks(hours)
    plt.xlabel('Hour')
    plt.ylabel('Sales in USD ($)')
    plt.grid()
    plt.show()

def plot_quantity_per_product(df):
    products = [product for product, df in df.groupby('Product')]
    quantity_ordered = df.groupby(['Product']).sum()['Quantity Ordered']
    plt.bar(products, quantity_ordered)
    plt.xticks(products, rotation=45, size=8, ha='right')
    plt.xlabel('Product')
    plt.ylabel('Quantity Ordered')
    plt.show()

def plot_quantity_price_per_product(df):
    products = [product for product, df in df.groupby('Product')]
    quantity_ordered = df.groupby(['Product']).sum()['Quantity Ordered']
    price_each = df.groupby(['Product'])['Price Each'].mean()

    fig, ax = plt.subplots()
    ax2 = ax.twinx()

    ax.bar(products, quantity_ordered, color='g')
    ax2.plot(products, price_each, color='b')

    ax.set_xticks(products)
    ax.set_xticklabels(products, rotation=45, size=8, ha='right')
    ax.set_xlabel('Product')
    ax.set_ylabel('Quantity Ordered', color='g')
    ax2.set_ylabel('Price Each', color='b')
    ax2.ticklabel_format(style='plain', axis='y')
    plt.show()

