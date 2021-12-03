def dp(i,j,m,n,grid):
    if i>= m or j>=n or grid[i][j]=='#' :
        return 0
    elif(i==m-1 and j==n-1):
        return 1
    else:
        return dp(i+1,j, m,n,grid) + dp(i,j+1,m,n,grid)
    


def count_paths(m,n,blocks):
    '''
    

    Parameters
    ----------
    m : int
        number of rows
    n : int
        number of columns
    blocks : list
        list of tuples with block coordinates

    Returns
    -------
    int
        Number of paths

    '''
    assert isinstance(m,int) and isinstance(n,int)
    assert isinstance(blocks,list)

    grid = [['.']*n for i in range(m)]
    for i,j in blocks:
        assert i<n and j<m and i>=0 and j>=0
        
        grid[i][j] = '#'
    
    if grid[0][0] == '#':
        return 0
    
    return dp(0,0,m,n,grid)
    
        
    
    
    