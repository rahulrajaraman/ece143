import pandas as pd

def add_month_yr(df):
    '''
    

    Parameters
    ----------
    df : pandas.DataFrame
        survey.csv dataframe

    Returns
    -------
    df : pandas.DataFrame
        Dataframe with month-yr column

    '''
    assert isinstance(df, pd.DataFrame)    
    df['month-yr'] = pd.to_datetime(df['Timestamp']).dt.strftime('%b-%Y')
    #df =df.set_index('ID')
    return df

def fix_categorical(x):
    '''
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    x : pandas.DataFrame
        Dataframe with ordered month-yr as categorical dtype
        

    '''
    assert isinstance(x, pd.DataFrame)
    x['month-yr'] = pd.Categorical(x['month-yr'], categories = list(x['month-yr'].unique()), ordered = True)
    return x
