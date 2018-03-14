import pandas as pd


def get_toy_data():
    toy_data = {
        'a': [1, 2, 2],
        'b': ['cat', 'cat', 'dog'],
        'c': ['yes', 'yes', 'no']
    }

    return pd.DataFrame(toy_data)
