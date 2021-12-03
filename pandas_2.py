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

    
#Pandas 3 continuation
def count_month_yr(x):
    '''
    

    Parameters
    ----------
    df : pandas.DataFrame
        data loaded from survey_data.csv

    Returns
    -------
    new_df : pandas.DataFrame
        The count of data in each year-month

    '''
    assert isinstance(x, pd.DataFrame)
    return x.groupby(x['month-yr']).count().iloc[:,0:1]
    
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

    
df = pd.read_csv('survey_data.csv', header = 0)
df = add_month_yr(df)
print(fix_categorical(df))