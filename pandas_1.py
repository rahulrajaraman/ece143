import pandas as pd

def split_count(x):
    '''
    

    Parameters
    ----------
    s : pandas.Series
        Series with column containing lists

    Returns
    -------
    df_counts : pandas.Dataframe
        Counts of each element occuring in the series

    '''
    assert isinstance(x,pd.Series)
    df = pd.DataFrame(x)
    df = df.rename({'Is there anything in particular you want to use Python for?':'topic'}, axis = 'columns')
    df = df.topic.str.split(', ', expand = True)
    series = pd.Series(df.to_numpy().flatten())
    df_counts = pd.DataFrame(series.value_counts())
    df_counts = df_counts.rename({0:'count'}, axis = 'columns')
    
    return df_counts.iloc[::-1]

