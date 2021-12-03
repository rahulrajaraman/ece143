def get_trapped_water(seq):
    '''
    

    Parameters
    ----------
    seq : list
        list of blocks in the structure

    Returns
    -------
    volume : int
        units of water stored

    '''
    assert isinstance(seq,list)
    l = len(seq)
    assert l>2
    x = [[0,0] for i in range(l)]
    
    left = seq[0]
    volume = 0
    
    i = 1
    while i < len(seq) -1:
        left = seq[i]
        right = seq[i]
        for j in range(i):
            if seq[j] > left:
                left = seq[j]
        
        for j in range(i+1,len(seq)):
            if seq[j] > right :
                right = seq[j]
        
        volume += min(right,left)  - seq[i]
        i+=1
                
                
                
        
    return volume


