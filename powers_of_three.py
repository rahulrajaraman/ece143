import itertools
def get_power_of3(number):
    '''
     Parameters
    ----------
    number : int from 1-40
        Any integer between 1-40

    Returns
    -------
    A list of length 4 consisting of integers

    '''
    assert isinstance(number, int)
    assert number>=0 and number < 41
    
    range_set = [-1, 0, 1]
    values_of3 = [1,3,9,27]
    powers = list(itertools.product(range_set, repeat=4))
    
    for answer in powers:
        if ((answer[0]*values_of3[0])+(answer[1]*values_of3[1])+(answer[2]*values_of3[2])+ (answer[3]*values_of3[3])) == number:
            decomposition = answer
            break
    return list(decomposition)
        
