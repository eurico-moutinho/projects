# eda

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

def show_data(path):
    df = pd.read_csv(path)
    return df

def describe_data(df):
    print(df.head(20).to_string(index=False), '\n')
    print('------------------------------------------------------------------------------------------------------------------------\n')
    print('description:\n', df.describe())
    print('------------------------------------------------------------------------------------------------------------------------\n')
    print(df.info())
    print('------------------------------------------------------------------------------------------------------------------------\n')
    print(f"Number of duplicate rows: {df.duplicated().sum()}")
    print('------------------------------------------------------------------------------------------------------------------------\n')
    print('Male', df['Gender'].value_counts()['Male'])
    print('Female', df['Gender'].value_counts()['Female'])

def plot_histogram(df, columns, hue=None, bins=30):
    for col in columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df, x=col, bins=bins, kde=True, color='skyblue', hue=hue, multiple='stack', edgecolor='black', linewidth=1.2)
        plt.title('Distribution of ' + col)
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.show()

def plot_bar_chart(df, column, hue=None):
    plt.figure(figsize=(10, 6))
    sns.catplot(x=column, kind='count', legend=True, hue = hue, data=df, height=5, aspect=1.5)
    plt.title('Frequency of ' + column)
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

def plot_scatter_plot(df, x, y, hue=None):
    sns.lmplot(data=df,
               x=x,
               y=y,
               hue=hue,
               palette='Set2',
               legend=True,
               height=6,
               aspect=1.4,
               fit_reg=False)

def plot_boxplot(df, x, y):
    sns.boxplot(data=df,
                  x=x,
                  y=y,
                  palette='deep',
                  hue=x,
                  linewidth=1.5,
                  legend=False)
    plt.xticks(rotation=90)
    sns.set_theme(rc={"figure.figsize":(10, 6)})

def plot_heatmap(df):
    df['Gender_num'] = df['Gender'].map({'Male': 1, 'Female': 0})
    corr_matrix = df.select_dtypes(include=['int64', 'float64']).corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()