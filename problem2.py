def convert_hex_to_RGB (color_list):
    '''
    This program converts a list of color hex codes into a list of RGB tuples
    Argument : A list of strings should be given as argument. Please note that each 
    string should have 7 characters and must start with # and should be a 
    valid hexadecimal number 
    '''
    RGB_list = []
    assert isinstance(color_list, list)
    for element in color_list:
        assert len(element) == 7
        element = element.upper()
        assert element[0] == '#'
        R = element[1:3]
        G = element[3:5]
        B = element[-2::]
        assert  ((47<ord(R[0])<58) or (64<ord(R[0])<71))
        assert  ((47<ord(R[1])<58) or (64<ord(R[1])<71))
        assert  ((47<ord(G[0])<58) or (64<ord(G[0])<71))
        assert  ((47<ord(G[1])<58) or (64<ord(G[1])<71))
        assert  ((47<ord(B[0])<58) or (64<ord(B[0])<71))
        assert  ((47<ord(B[1])<58) or (64<ord(B[1])<71))
        RGB_list.append((int(R,16),int(G,16),int(B,16)))
    return RGB_list   
    

