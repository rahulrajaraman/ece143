import random
import itertools


 
def get_sample(nbits=3, prob=None, n =1):
    '''
    
    Parameters
    ----------
    nbits : int, optional
        number of bits. The default is 3.
    prob : Dict, optional
        Contains weights of the  combinations. The default is None.
    n : int optional
        Number of elements to be given as output. The default is 1.

    Returns
    -------
    TYPE
        list 

    '''
    assert isinstance(n,int) and n>0
    assert isinstance(nbits,int) and nbits >0
    list_combinations = list(itertools.product(range(2), repeat = nbits)) ;
    if prob is None:
        return random.choices(list_combinations, k =n);
    else:
        assert len(list_combinations) == len(list(prob.keys()))
        return random.choices(list_combinations, weights = list(prob.values()), k =n);
        
