# eda.py

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def show_data(path):
    df = pd.read_csv(path)
    return df

def bar_chart(df, column, hue=None):
    plt.figure(figsize=(10, 6))
    sns.catplot(x=column, kind='count', legend=True, hue = hue, data=df, height=5, aspect=1.5)
    plt.title('Heart Disease Frequency vs Sex')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

def crosstab(df):
    return pd.crosstab(index=df.target, columns=df.sex)

def age_vs_max_heart_rate(df):
    plt.figure(figsize=(10,6))

    plt.scatter(df.age[df.target==1], 
                df.thalach[df.target==1], 
                c="salmon")

    plt.scatter(df.age[df.target==0], 
                df.thalach[df.target==0], 
                c="lightblue")

    plt.title("Heart Disease in function of Age and Max Heart Rate")
    plt.xlabel("Age")
    plt.legend(["Disease", "No Disease"])
    plt.ylabel("Max Heart Rate")

def histogram(df, columns):
    sns.set(style='whitegrid')

    plt.figure(figsize=(15, 10))
    for i, feature in enumerate(columns):
        plt.subplot(2, 3, i + 1)
        sns.histplot(df[feature], bins=20, kde=True)
        plt.title(feature)
    plt.tight_layout()
    plt.show()

def remove_outliers(df, columns):
    Q1 = df[columns].quantile(0.25)
    Q3 = df[columns].quantile(0.75)
    IQR = Q3 - Q1

    condition = (df[columns] < (Q1 - 1.5 * IQR)) | (df[columns] > (Q3 + 1.5 * IQR))
    filtered_df = df[~condition.any(axis=1)]

    return filtered_df
    
def scaling(filtered_df, columns):

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(filtered_df[columns])
    scaled_df = pd.DataFrame(scaled_features, columns=columns, index=filtered_df.index)
    filtered_df.loc[:, columns] = scaled_df.astype('float64')

    return filtered_df

def heatmap(df):
    corr_matrix = df.corr()
    plt.figure(figsize=(15, 10))
    sns.heatmap(corr_matrix, 
                annot=True, 
                linewidths=0.5, 
                fmt= ".2f", 
                cmap="YlGnBu")