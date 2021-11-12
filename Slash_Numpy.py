import numpy as np
import random 


def gen_rand_slash(m=6,n=6, direction = 'back'):
    '''
    

    Parameters
    ----------
    m : int, optional
        Number of rows in the matrix. The default is 6.
    n : int, optional
        Number of columns in the matrix. The default is 6.
    direction : string, optional
        The direction of the slash. It should be forward or backward. The default is 'back'.

    Returns
    -------
    result_mat : 2Dnumpy array of int
        The slash is depicted by 1's and 

    '''
    assert isinstance(m,int) and isinstance(n,int)
    assert m>1 and n>1
    assert direction == 'back' or direction == 'forward'
    
    result_mat = np.zeros((m,n), dtype = int)
    row = random.randint(0, m-2)
    col = random.randint(0,n-2)

    
    if direction == 'back':
        result_mat[row,col] = 1
        
        x = row +1
        y = col +1
        for i in range(random.randint(1,min(m-row-1, n-col-1))):
            
            result_mat[x+i,y+i] = 1
            result_mat[x,y] = 1
    
    else:
        row = random.randint(1, m-1)
        
        print(row,col)
        result_mat[row,col] = 1
        x = row -1
        y = col +1
        for i in range(random.randint(1,min(row, n-col-1))):
            result_mat[x-i, y+i] = 1
            
    return result_mat

