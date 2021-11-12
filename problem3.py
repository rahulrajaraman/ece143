def compute_average_word_length(instring, unique=False):
    '''
    This program is to compute the average word length in the paragraph
    There are two arguments, one is the paragraph as a string. The other argument is a 
    boolean value which will specify if a duplicates are to be counted (False) or not(True)
    It is set to False by default.
    punctuations will give assertion errors
    '''
    assert isinstance(instring, str)
    assert isinstance(unique , bool)
    word_list = instring.split(" ")
    if unique is True:
        sum = 0
        unique_words = set(word_list)
        for each_word in unique_words:
            sum = sum + len(each_word)
        return sum/len(unique_words)
        
    else:
        sum = 0
        for each_word in word_list:
            sum = sum + len(each_word)
        return sum/len(word_list)

