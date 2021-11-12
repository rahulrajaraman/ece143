def get_average_word_length(words):
    '''
    
    Parameters
    ----------
    words : list
        List of words to determine average word length 

    Returns
    -------
    float
        returns average word length

    '''
    assert isinstance(words,list)
    word_count = 0
    letter_count = 0
    for word in words:
        assert word.isalpha()
        word_count+=1
        letter_count+=len(word)
        
    return letter_count/word_count
    
def get_longest_word(words): 
    '''
    

    Parameters
    ----------
    words : list
        List of words

    Returns
    -------
    word
    
    The longest word in the wordlist

    '''
    assert isinstance(words,list)
    max_letter_count = 0
    
    for word in words:
        assert word.isalpha()
        if len(word) > max_letter_count:
            longest_word = word
            max_letter_count = len(longest_word)
    
    return longest_word
    
def get_longest_words_startswith(words,start):
    '''
    
    Parameters
    ----------
    words : list 
        List of words
    start : chr
        the first letter of the longest word 

    Returns
    -------
    str
    
    The longest word that starts with character 'start' is returned

    '''
      
    assert isinstance(words,list) 
    assert isinstance(start,str) and len(start) ==1
    assert start.isalpha()
    max_word_count = 0
    for word in words:
        assert word.isalpha()
        if word[0] == start and len(word) > max_word_count:
            longest_word = word
            max_word_count = len(longest_word)
    
    return longest_word
    
    
def get_most_common_start(words):
    '''
    

    Parameters
    ----------
    words : list
        List of words

    Returns
    -------
    chr
    Returns the most common first letter in the word list

    '''
    
    
    assert isinstance(words,list)
    char_array = [chr(i) for i in range(ord('a'),ord('z')+1)]
    letter_start_count = dict(zip(char_array, [0]*len(char_array)))    
    
    for word in words:
        assert word.isalpha()
        letter_start_count[word[0]] += 1
        
        
    max_val = 0
    for key, val in letter_start_count.items():
        if val > max_val:
            max_key = key 
            max_val = val
            
    return max_key
        
    
def get_most_common_end(words):
    '''
    

    Parameters
    ----------
    words : list
        List of words

    Returns
    -------
    max_key : chr
        Returns the most common last letter in the word list

    '''
    
    
    
    char_array = [chr(i) for i in range(ord('a'),ord('z')+1)]
    letter_end_count = dict(zip(char_array, [0]*len(char_array)))    
    
    for word in words:
        assert word.isalpha()
        letter_end_count[word[-1]] += 1
        
    max_val = 0
    for key,val in letter_end_count.items():
        if val > max_val:
            max_key = key 
            max_val = val
            
    return max_key



