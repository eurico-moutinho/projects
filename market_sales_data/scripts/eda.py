import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

def demographics_graph(df):
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    plt.pie(df['Gender'].value_counts(), labels=df['Gender'].value_counts().index, autopct='%1.1f%%', shadow=True, startangle=90, explode=(0, 0.1))
    plt.title('Distribution of Gender')

    plt.subplot(1, 2, 2)
    ax = sns.histplot(df, x='Customer type', color='skyblue', hue='Gender', multiple='stack', edgecolor='black', linewidth=1)
    plt.title('Distribution of Customer Type')
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.show()

def stats(data, column):
    avg = data.groupby('Product line')[column].mean()
    std = data.groupby('Product line')[column].std()
    var = data.groupby('Product line')[column].var()

    print('Average Price:', avg, '\n')
    print('Standard Deviation:', std, '\n')
    print('Variance:', var, '\n')

def price_avg_graph(df):
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Product line', y='Unit price', data=df, palette='Set2', hue='Product line', legend=False, errorbar=None)
    plt.xticks(rotation=45)
    plt.title('Average Price of Products')
    plt.xlabel('Product line')
    plt.ylabel('Average Price')
    for i in ax.containers:
        ax.bar_label(i, padding=3, fmt='%.2f')
    plt.show()

def sales_quantity_graph(df):
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Product line', y='Quantity', estimator=sum, data=df, palette='Set2', hue='Product line', legend=False, errorbar=None)
    plt.xticks(rotation=45, ha='right')
    plt.title('Sales Quantity of Products')
    plt.xlabel('Product line')
    plt.ylabel('Quantity')
    for i in ax.containers:
        ax.bar_label(i, padding=3)
    plt.show()

def revenue_graph(df, type):
    plt.figure(figsize=(10, 6))
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax2 = ax1.twinx()
    sns.barplot(x='Product line', y='Total', data=df, estimator=sum, palette='Set2', ax=ax1, hue=type, errorbar=None)
    ax1.set_ylabel('Revenue by ' + type)

    sns.lineplot(
        x='Product line',
        y='Total',
        data=df,
        estimator=sum,
        ax=ax2,
        label='Total Revenue',
        legend=False,
        errorbar=None
    )
    ax2.set_ylabel('Total Revenue', color='blue')
    ax2.yaxis.label.set_rotation(270)
    ax2.yaxis.set_label_coords(1.1, 0.5)
    ax2.tick_params(axis='y', labelcolor='blue')

    bar_handles, bar_labels = ax1.get_legend_handles_labels()
    line_handles, line_labels = ax2.get_legend_handles_labels()

    ax1.legend(bar_handles + line_handles, bar_labels + line_labels, loc='lower right')

    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
    plt.title('Revenue of Products')
    plt.xlabel('Product line')
    plt.tight_layout()
    plt.show()

def sales_over_time_graph(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Month', y='Total', data=df, estimator=sum, palette='Set2', hue='Year', errorbar=None)
    plt.title('Sales Over Time')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.show()

def rating_by_gender(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Gender', y='Rating', data=df, palette='Set2', hue='Gender', legend=False, linewidth=1)
    plt.title('Rating by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Rating')
    plt.show()