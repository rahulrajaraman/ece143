def write_chunks_of_five(words,fname):
    '''
    
    Parameters
    ----------
    words : List of strings
        It is a list comprising of words
    fname : string
        output filename string

    Returns
    -------
    file object

    '''
    assert isinstance(words, list)
    assert isinstance(fname, str)
    assert fname.endswith(".txt")
    with open(fname, 'w') as f:
        s = " "
        word_lists = [s.join(words[i:i+5]) for i in range(0, len(words), 5)]
        print(word_lists)
        
        for line in word_lists:
            f.write(line + '\n')
    
    return f

        