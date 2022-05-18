import pandas as pd
from sklearn.decomposition import PCA
from typing import Union

def remove_outliers(df : pd.DataFrame,inplace=False) -> Union[pd.DataFrame,None]:
    """
    Remove outliers from the dataframe passed in parameter. An outlier is defined as
    any value whose speal width > 2.5cm and whose petal length is > 2.0cm.
    
    Args:
        df (pd.DataFrame): dataframe to remove outliers from
        inplace (bool): whether to perform the operation inplace. Default to false
    
    Return:
        Union[None,pd.DataFrame]: either copied dataframe or None (if inplace)
        
    """
    if not inplace:
        df = df.copy()
    df.drop(df.index[(df['sepal width (cm)'] < 2.5) & (df['petal length (cm)'] < 2.0)],inplace=True)
    if not inplace:
        return df
    
def run_PCA(df : pd.DataFrame) -> pd.DataFrame:
    """
    Perform pca dimension reduction (3 dimensions) on the 'sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
       'petal width (cm)' of the df 
    
    Args:
        df (pd.DataFrame): dataframe to remove outliers from
    
    Returns:
        [pd.DataFrame] : pca-reduced version of the
    """
    # One should separate computation and plotting functions
    X_reduced = PCA(n_components=3).fit_transform(df.drop(columns=['target']))
    reduced_df = pd.DataFrame(X_reduced)
    return reduced_df
