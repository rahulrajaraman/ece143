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


def gather_values(x):
    '''
    Parameters
    ----------
    x : list
        list of variables as result from samplebitstring 1

    Returns
    -------
    value_map : dict
        says 1/0 from sample bitstring 2 and and creates a list eual to 
        number of times the element is encountered.

    '''
    assert isinstance(x,list)
    map_bitstring_dict = map_bitstring(x)
    assert isinstance(map_bitstring_dict, dict)
    value_map = dict()
    for ele in x:
        val = map_bitstring_dict[ele]
        value_map.setdefault(ele,[]).append(val)
        
    return value_map


