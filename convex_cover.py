import numpy as np
def find_convex_cover(pvertices,clist):
    '''
    

    Parameters
    ----------
    pvertices : np.array
        array of coordinates of vertices
    clist : list
        list of coord of corcle centers.

    Returns
    -------
    list
        list of radii for given circles

    '''
    assert isinstance(pvertices,np.ndarray)
    assert isinstance(clist,list) 
    centers = np.array(clist)
    d = centers[:,None,:] - pvertices
    di = np.sum(d*d,axis =2).astype(float)
    
    dist = np.sqrt(di)
    min_dist = np.amin(dist, axis =0)
    min_dist_idx = np.argmin(dist,axis=0)
    
    circle_dict = {i : [] for i in range(7)}
    ans = {i : 0 for i in range(7)}
    for i in range(len(min_dist)):
        circle_dict[min_dist_idx[i]].append(min_dist[i])
        
    for key,val in circle_dict.items():
        if not len(val) == 0:
            ans[key] = max(val)
        
        
    return list(ans.values())

'''
pvertices = np.ndarray([[ 0.573,  0.797],           
                        [ 0.688,  0.402],                                                              
                        [ 0.747,  0.238],                                                              
                        [ 0.802,  0.426],                                                              
                        [ 0.757,  0.796],                                                              
                        [ 0.589,  0.811]] )                                                           
                                                                                                       
clist = [(0.7490863467660889, 0.4917635308023209),                                       
              (0.6814339441396109, 0.6199470305156477),                                                
              (0.7241617773773865, 0.6982813914515696),                                                
              (0.6600700275207232, 0.7516911829987891),                                                
              (0.6315848053622062, 0.7730550996176769),                                                
              (0.7348437356868305, 0.41342916986639894),                                               
              (0.7597683050755328, 0.31729154508140384)]   
'''