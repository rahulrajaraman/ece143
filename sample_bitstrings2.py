def map_bitstring(x):
    '''
    Parameters
    ----------
    x : list
        list of bitstrings

    Returns
    -------
    Dict

    '''
    assert isinstance(x,list) ;
    
    map_bits = dict()
    for i in x:
        
        count_zeros = 0
        count_1 =0
        for j in i:
            if j == '0':
                count_zeros = count_zeros+1
            else:
                count_1 = count_1+1
        if count_zeros>count_1:
            map_bits[i] = 0
        else:
            map_bits[i] = 1
            
    return map_bits

