def encrypt_message(message,fname):
    
    '''
       Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
       name of a text file source for the codebook, generate a sequence of 2-tuples that
       represents the `(line number, word number)` of each word in the message. The output is a list
       of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 
       
       :param message: message to encrypt
       :type message: str
       :param fname: filename for source text
       :type fname: str
       :returns: list of 2-tuples
    '''
    assert isinstance(message, str) and isinstance(fname,str)
    indices = []
    with open(fname) as f:
        lines = f.readlines()
        for word in message.split():
            for i in range(len(lines)):
                a = (0,0)
                each_line = lines[i].split()
                if word in each_line:
                    a=(i+1,each_line.index(word)+1)
                    if a in indices:
                        continue
                    indices.append(a)
                    break
            if a == (0,0):
                assert False 
        
        return indices
    
def decrypt_message(inlist,fname):
      '''
      Given `inlist`, which is a list of 2-tuples`fname` which is the
      name of a text file source for the codebook, return the encrypted message. 
      
      :param message: inlist to decrypt
      :type message: list
      :param fname: filename for source text
      :type fname: str
      :returns: string decrypted message
      '''
      assert isinstance(fname,str) and isinstance(inlist, list)
      s = []
      with open(fname) as f:
          lines = f.readlines()
          for i in inlist:
              g = lines[i[0]-1].split()
              s.append(g[i[1]-1])
              d = ' '.join(s)
      return d
        #print(s)
      

                    