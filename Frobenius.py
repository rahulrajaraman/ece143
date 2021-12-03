import numpy as np

def solvefrob(coeffs,b):
    '''
    

    Parameters
    ----------
    coeffs : list
        list of coefficients for equation
    b : int
        constant on other side of equality

    Returns
    -------
    ret : list
        lis tof tuples that are solution for given equation

    '''
    assert isinstance(coeffs, list) and isinstance(b,int)
    for c in coeffs:
        assert isinstance(c, int) and c>0 and    b>0  
        
    
    
    max_coeffs = [list(range(b//coeffs[i]+1)) for i in range(len(coeffs))]
    
    for i in range(len(max_coeffs)):
        max_coeffs[i]=np.array(max_coeffs[i],dtype=int)
        max_coeffs[i]=max_coeffs[i]*coeffs[i]
    for i in range(len(max_coeffs)):
        count=len(max_coeffs)-i-1
        if not(count==0):
            for j in range(count):
                max_coeffs[i] = np.expand_dims(max_coeffs[i],axis=-1)
                
   
                
    result = max_coeffs[0]
    for i in range(1,len(max_coeffs)):
        result = result + max_coeffs[i]
    
    index = np.where(result == b)
    ret = []
    for i in range(len(index[0])):
        x = []
        for j in range(len(index)):
            x.append(index[j][i])
        ret.append(tuple(x))
    
    return ret
