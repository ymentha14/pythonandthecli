import mpl_toolkits.mplot3d  # noqa: F401
import pandas as pd
import matplotlib.pyplot as plt

def plot_3d(reduced_df : pd.DataFrame,target: pd.Series, ax: plt.axes):
    """
    Plot the pca-reduced dataframe on a 3-d plot
    
    Args:
        reduced_df (pd.DataFrame): dataframe obtained after a dimension reduction (3 dimensions)
        target (pd.Series): target designating the class of each sample
        ax (plt.axes): matplotlib ax
    """
    ax.scatter(
        reduced_df.iloc[:, 0],
        reduced_df.iloc[:, 1],
        reduced_df.iloc[:, 2],
        c=target,
        cmap=plt.cm.Set1,
        edgecolor="k",
        s=40,
    )
    ax.set_title("First three PCA directions")
    ax.set_xlabel("1st eigenvector")
    ax.w_xaxis.set_ticklabels([])
    ax.set_ylabel("2nd eigenvector")
    ax.w_yaxis.set_ticklabels([])
    ax.set_zlabel("3rd eigenvector")
    ax.w_zaxis.set_ticklabels([])
    
def sanity_outlier_plot(df : pd.DataFrame, ax : plt.axes):
    """
    Display a scatter plot of sepal width vs petal length for visual
    inspection
    
    Args:
        df (pd.DataFrame): dataframe with potential outliers
        ax (plt.axes): ax to plot on
    """
    df.plot.scatter(x='sepal width (cm)',y='petal length (cm)',ax=ax)
