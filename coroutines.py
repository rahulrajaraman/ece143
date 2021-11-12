from time import sleep
import random
from datetime import datetime
import itertools as it
import types
 
def producer():
    '''
    
    Yields
    ------
    datetime object
        Difference between current time and start time

    '''
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0,0.2))
        yield datetime.now()-starttime

def tracker(p,limit):
    '''
    Parameters
    ----------
    p : generator object
        p is an object of producer(). It tracks time
    limit : int
        The number of odd numbered seconds that is to be tracked

    Returns
    -------
    None.

    '''
    assert isinstance(limit,int) and limit > 0
    assert isinstance(p,types.GeneratorType)
    old_limit = limit
    count = 0
    while count < old_limit:
        if next(p).seconds%2 == 1:
            count= count + 1
        limit = (yield count) 
        if limit is not None:
            old_limit = limit 
       
        
p = producer()
           
            


