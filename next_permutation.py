def next_permutation(t:tuple) -> tuple:
    '''
    Parameters
    ----------
    t : tuple
        tuple of numbers

    Returns
    -------
    tuple
        next lexicographic element.

    '''
    assert isinstance(t, tuple)
    for i in t:
        assert isinstance(i, int)
    assert len(t) > 0 
    assert len(t) == len(set(t))
    
    n = len(t)
    if(n<2):return t
        
    t = list(t)
    i= n-2
    while(i>=0 and t[i] >= t[i+1]):
        i-=1
        
    if i==-1: 
    
        t.sort()
    else:
        j=i+1
        while j<n and t[j]>t[i]: 
            j+=1
        t[i],t[j-1] = t[j-1],t[i]
        t[i+1:] = t[i+1:][::-1]
    return tuple(t)

