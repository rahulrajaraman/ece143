def is_string_integer(str_or_int):
    '''
    This function takes a single character as an argument and 
    returns True if it is an integer and False otherwise
    Argument : Single character string
    '''
    assert isinstance(str_or_int, str)
    assert len(str_or_int) == 1
    
    if 47 < ord(str_or_int) < 58:
        return True
    else:
        return False
        
        

