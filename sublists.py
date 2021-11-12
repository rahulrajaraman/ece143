import itertools

def all_sublists(x):
    '''
    Parameters
    ----------
    x : list
        list of integers with unique elements

    Returns
    -------
    return_list : list
        A list of all sublists for the given list of integer x

    '''
    assert isinstance(x,list)
    assert len(x) != 0
    assert len(x) == len(set(x))
    
    i=1
    sublists = []
    while i <= len(x):
        sublists.extend(list(itertools.combinations(x,i)))
        i=i+1
    
    return_list = [list(i) for i in sublists]
    
    return return_list

