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


def threshold_values(seq,threshold=1):
    '''
    

    Parameters
    ----------
    seq : list
        list of bitstrings from sample bitstrings1
    threshold : int, optional
        The number of most frequent bitsrtings turned to 1. The default is 1.

    Returns
    -------
    return_dict : dict
        Returns a dictionary with value 1 for 'threshold' number of elements and 0 for 
        everything else. When two bitstrings has same number of 1's it takes the smaller botstring value

    '''
    assert isinstance(seq,list)
    assert isinstance(threshold, int) and threshold > 0
    map_bits_dict = map_bitstring(seq)
    thres_val_sum = dict()
    return_dict = dict()
    gather_val_dict = gather_values(seq)
    for key, value in gather_val_dict.items():
        thres_val_sum[key] = len(value)*value[0]
        return_dict[key] = 0
    
    i = 0
   
    while i < threshold:
        max_val = -1
        for key,value in thres_val_sum.items():
            
            if value > max_val:
                max_val = value
                max_key = key
                
            if value == max_val:
                if (int(key,2) < int(max_key,2)):
                    max_key = key
               
            
        print(max_key)
        thres_val_sum[max_key] = -2
        return_dict[max_key] = 1 
        i = i+1
            
    
         
    return return_dict


    