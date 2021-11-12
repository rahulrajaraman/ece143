import csv
def write_columns(data,fname):
    '''
    Parameters
    ----------
    data : list
        List of int/float numbers
    fname : filename string
        filename for csv

    Returns
    -------
    csvfile - fileobject

    '''
    assert isinstance(data,list)
    assert isinstance(fname,str)
    
    with open(fname,'w') as csvfile:
        for data_value in data:
            writer = csv.writer(csvfile, delimiter=",")
            assert isinstance(data_value,int) or isinstance(data_value,float)
            writer.writerow([round(data_value,2),round(data_value**2,2),round((data_value+data_value**2)/3, 2)])
    
    return csvfile


