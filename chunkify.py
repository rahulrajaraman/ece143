import os

def split_by_n(fname,n=3):
    '''
    

    Parameters
    ----------
    fname : string
        The file name (path) of the source
    n : int, optional
        number of chunks to be split. The default is 3.

    Returns
    -------
    None.

    '''
    assert isinstance(fname, str) and isinstance(n,int)
    assert n>0
    
    size = os.path.getsize(fname)
    i = 0
    file = open(fname,'r')
    lines = file.readlines()
    file.close()
    j=0
    while j < n:
        s = ''
        g = lines[0]
        f = open(fname+"_00"+str(j)+".txt", 'wt')
        ele = len(lines)
        i=0
        while i<ele:  
            #g+=lines[i+1]
            if len(s.encode('utf-8')) < size/n:
                s+=lines[0]
                lines.pop(0)
            else:
                break
            i+=1
        f.write(s)
        f.close()
        print(os.path.getsize(fname+"_00"+str(j)+".txt"))
        j+=1
        

    
    