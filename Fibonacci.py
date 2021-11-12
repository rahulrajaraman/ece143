def fibonacci(n):
    '''
    Parameters
    ----------
    n : int
        number of elements in fibonacci series

    Yields
    ------
    i : int
        elements in fibonacci seires

    '''
    assert isinstance(n,int)
    assert n>2
    i=2
    F = [1,1]
    
    while(i<n):
        F.append(F[i-2] + F[i-1])
        i=i+1
    for i in F:
        yield i
    