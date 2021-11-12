import random
from collections import defaultdict

def multinomial_sample(n,p,k=1):
    '''
    

    Parameters
    ----------
    n : int
        Number of trials in each sample
    p : list
        list of probabilities/weights
    k : int, optional
        The number of samples in output. The default is 1.

    Returns
    -------
    final_list : list
        list of all trials in sample

    '''
    assert isinstance(n,int) and isinstance(k,int)
    assert n>0 and k>0
    assert isinstance(p,list)
    sum =0
    for i in p:
        assert isinstance(i,int) or isinstance(i,float)
        sum +=i
    assert sum==1
    num_list = [i for i in range(len(p))]
    i=0
    final_list = []
    while i<k:
        ele_count = defaultdict(lambda:0)
        trial_list = random.choices(num_list, weights=p, k=n)
        for j in trial_list:
            ele_count[j]+=1
        final_list.append(list(ele_count.values()))
        i+=1
    
    return final_list
        
        