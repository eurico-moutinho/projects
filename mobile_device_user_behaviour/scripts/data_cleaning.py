# data_cleaning.py

import pandas as pd


def clean_data(data):
    # remove rows with null values
    data = data.dropna()

    # remove rows with empty values
    data = data.dropna(how='all')
    return data