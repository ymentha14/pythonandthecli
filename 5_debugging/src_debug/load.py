import pandas as pd
from sklearn import datasets
from pdb import set_trace

def load_iris_df():
    """
    Load the iris data from scikit learn as a pandas dataframe
    """
    iris = datasets.load_iris()
    column_names = iris['feature_names']

    # The list has only 4 elements! probably a typo
    set_trace()
    last_name = column_names[30]

    iris_df = pd.DataFrame(iris['data'],columns=column_names)
    iris_df['target'] = iris.target
    return iris_df

def load_magnolia_df():
    """
    Function for debug features puprpose
    """
    # datasets has no function load_magnolia
    N_flowers = 4
    iris = datasets.load_magnolia()
    column_names = iris['feature_names']

    # The list has only 4 elements! probably a typo
    set_trace()
    last_name = column_names[30]

    iris_df = pd.DataFrame(iris['data'],columns=column_names)
    iris_df['target'] = iris.target
    return iris_df