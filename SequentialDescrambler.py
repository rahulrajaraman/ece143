import itertools
from collections import Counter
def descrambler(w,k):
    '''
    

    Parameters
    ----------
    w : str
        a string from ehich words are made
    k : tuple
        the word length split for sentence.

    Yields
    ------
    i : str
        Sentence made of given characters according to split

    '''
    assert isinstance(w,str)
    assert isinstance(k,tuple)
        
    word_dict = dict()
    with open('/tmp/google-10000-english-no-swears.txt') as f:
        for words in f.readlines():
            word_dict[words] = len(words) -1
            
    inv_word = dict()
        
    for key,val in word_dict.items():
        inv_word[val] = inv_word.get(val , []) + [key]
    
    sorted_values = dict()
    for length in k:
        for char in inv_word[length]:
            sorted_values.setdefault(length, []).append("".join(sorted(char.replace('\n',''))))
    
    sort_map_dict = dict()
    for i in k:
        for word in inv_word[i]:
            sort_map_dict[word.replace('\n','') ] = "".join(sorted(word.replace('\n','')))
    
    
    
    final_word_list = dict()
    combo_words = dict()    
    S = []
    
    for i in range(len(k)):
        S.append(list(itertools.combinations(w,k[i])))    
    word_list_comb = []
    for i in range(len(list(S))):
        for j in range(len(list(S[i]))):            
            t = ''.join(sorted(S[i][j]))
            S[i][j] = t
            
    
    for i in range(len(k)):
        S[i] = list(set(S[i]))
    
    wordlist = []
    
    for i in range(len(k)):
        S[i] = [word for word in S[i] if word in sorted_values[k[i]]]
        
    word_combinations = list(itertools.product(*S))
    
    final_list = []
    for sentence in word_combinations:
        #print(sentence)
        p=''
        for j in range(len(k)):
            p += sentence[j]
            if Counter(p) == Counter(w):
                final_list.append(sentence)
                    
    final_list = list(set(final_list))
    answer1 = []
    answer = []
    correct_word_list = [] 
    final = []
    sentences_made = []
    #print("Final List")
    #print(final_list)
    for ele in final_list:
        for i in range(len(k)):
            correct_words = [key for key,val in sort_map_dict.items() if val==ele[i]]
            final.append(correct_words)
        temp = list(itertools.product(*final))
        final = []
        answer1.append(temp)
        
    for i in answer1:
        for j in i:
            p=''
            for k in range(len(j)):
                if not (k==len(j)-1):
                    p+=j[k]+' '
                else:
                    p+=j[k]
            yield p
            
    
    
