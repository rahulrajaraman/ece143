import collections 
import copy

class Polynomial:
    '''
    Polynomial Classes
    __init__ : Input is dict()
    
    '''
    def __init__(self, p):
        '''
        

        Parameters
        ----------
        p : dict
            dict of pwers:coefficients 

        Returns
        -------
        None.

        '''
        assert isinstance(p,dict)
        self._poly = p
        self._powers = list(p.keys())
        for i in self._powers:
            assert isinstance(i,int)
        self._coefficients = list(p.values())
        for i in self._coefficients:
            assert isinstance(i,int)
        self._coefficients=[x for _,x in sorted(zip(self._powers,self._coefficients))]
        self._powers=sorted(self._powers)
        
    def __add__(self,other):
        '''
        

        Parameters
        ----------
        other : Polynomial or int
            

        Returns
        -------
        TYPE Polynomial
            sum of two polynomials

        '''
        assert isinstance(self,Polynomial) 
        assert isinstance(other,Polynomial) or isinstance(other,int)
        p = dict()
        if isinstance(other,Polynomial):
            powers=list(set(self._powers+other._powers))
        else:
            powers=self._powers
        p=dict(zip(powers,[0]*len(powers)))
        for i in range(len(self._powers)):
            p[self._powers[i]]+=self._coefficients[i]
        if isinstance(other,Polynomial):
            for i in range(len(other._powers)):
                p[other._powers[i]]+=other._coefficients[i]
            if all([v==0 for v in p.values()]):
                return Polynomial(p)
            r=[]
            for key in p:
                if p[key]==0:
                    r.append(key)
            for i in r:
                    del p[i]
            result=Polynomial(p)
            return result
        else:
            p[0]+=other
            result=Polynomial(p)
            return result
                
                
        return Polynomial(p)
    
    def __sub__(self,other):
        '''
        

        Parameters
        ----------
        other : Polynomial or int
            

        Returns
        -------
        TYPE
            difference of two poly

        '''
        
        assert isinstance(self,Polynomial)
        assert isinstance(other,Polynomial) or isinstance(other,int)
        p = dict()
        if isinstance(other,Polynomial):
            other_copy=copy.deepcopy(other)
            for i in range(len(other_copy._coefficients)):
                other_copy._coefficients[i]= -1*other_copy._coefficients[i]
            powers=list(set(self._powers+other_copy._powers))
            p=dict(zip(powers,[0]*len(powers)))
            for i in range(len(self._powers)):
                p[self._powers[i]]=p[self._powers[i]] + self._coefficients[i]
            for i in range(len(other_copy._powers)):
                p[other_copy._powers[i]]+=other_copy._coefficients[i]
            if all([v==0 for v in p.values()]):
                return Polynomial(p)
            r = []
            for key in p:
                if p[key]==0:
                    r.append(key)
            for i in r:
                    del p[i]
            
            result=Polynomial(p)
            return result
        else:
            powers=self._powers
            input_dict=dict(zip(powers,[0]*len(powers)))
            for i in range(len(self._powers)):
                input_dict[self._powers[i]]+=self._coefficients[i]
            input_dict[0]-=other
            if all([v==0 for v in input_dict.values()]):
                return Polynomial(input_dict)
            to_remove=[]
            for key in input_dict:
                if input_dict[key]==0:
                    to_remove.append(key)
            for i in to_remove:
                    del input_dict[i]
            res=Polynomial(input_dict)
            return res
    
    def __rsub__(self,other):
        '''
        

        Parameters
        ----------
        other : TYPE
            DESCRIPTION.

        Returns
        -------
        results : TYPE
            DESCRIPTION.

        '''
        
        assert isinstance(self,Polynomial) and isinstance(other,int)
        #powers=self._powers
        p=dict(zip(self._powers,[0]*len(self._powers)))
        for i in range(len(self._powers)):
            p[self._powers[i]]+=self._coefficients[i]
        p[0]=other-p[0]
        if all([v==0 for v in p.values()]):
            return Polynomial(p)
        r=[]
        for key in p:
            if p[key]==0:
                r.append(key)
        for i in r:
            del p[i]
        result=Polynomial(p)
        return result
    
    def __eq__(self,other):
        assert isinstance(self,Polynomial)
        assert isinstance(other,Polynomial) or isinstance(other,int)
        if isinstance(other,Polynomial):
            other_p = collections.OrderedDict(sorted(other._poly.items()))
            self_p = collections.OrderedDict(sorted(self._poly.items()))
            if set(self._coefficients) == {0} and set(other._coefficients) == {0} :
                return True
            return self_p.keys() == other_p.keys() and self_p.values() == other_p.values() 
        
        else:
            if set(self._coefficients) == {0} and other == 0 :
                return True
            return self._powers == [0] and self._poly[0] == other  
            

    
    def __mul__(self, other):
        '''
        

        Parameters
        ----------
        other : Polynomial or int
            
        Returns
        -------
        results : Polynomial
            multiplication

        '''
        
        assert isinstance(self,Polynomial)
        assert isinstance(other,int) or isinstance(other,Polynomial)
        p = dict()
        
        if isinstance(other, Polynomial):
            results = Polynomial({0:0})
            
            for key1,val1 in self._poly.items():
                for key2, val2 in other._poly.items():
                    if key1+key2 in p.keys():                        
                        p[key1+key2] = p[key1+key2] + val1*val2
                    else:
                        p[key1+key2] =  val1*val2                    
                results = results + Polynomial(p)
                
                p.clear()
        else:
            res_coeff= []
            for val in self._coefficients:
                res_coeff.append(val*other)
                results = Polynomial(dict(zip(self._powers, res_coeff)))
            
        return results
    
    def __rmul__(self,other):
        '''
        

        Parameters
        ----------
        other : int
            multiplication with other classes

        '''
        
        assert isinstance(self,Polynomial) and isinstance(other,int)
        res_coeff = []
        for val in self._coefficients:
            res_coeff.append(val*other)
        res_dict = dict(zip(self._powers, res_coeff))
        if all([v==0 for v in res_coeff]):
            return Polynomial(res_dict)
        r=[]
        for key in res_dict:
            if res_dict[key]==0:
                r.append(key)
        for i in r:
            del res_dict[i]
        result=Polynomial(res_dict)
        return result
        
    
    
    def __radd__(self,other):
        '''
        

        Parameters
        ----------
        other : int
            addition with other classes
        Returns
        -------
        Polynomial
        '''
        
        assert isinstance(self,Polynomial) and isinstance(other,int)
        
        p=dict(zip(self._powers,[0]*len(self._powers)))
        for i in range(len(self._powers)):
            p[self._powers[i]]+=self._coefficients[i]
        p[0]+=other
        if all([v==0 for v in p.values()]):
            return Polynomial(p)
        r=[]
        for key in p:
            if p[key]==0:
                r.append(key)
        for i in r:
            del p[i]
        result=Polynomial(p)
        return result
            
    def __repr__(self):
        '''
        

        Returns
        -------
        string
            

        '''
        s = ''
        for i in range(len(self._powers)):
            if not(i==len(self._powers)-1):
                if self._powers[i]==0 and not(self._coefficients[i]==0):
                    s+=str(self._coefficients[i])+"+"
                elif self._powers[i]==1 and not(self._coefficients[i]==0):
                    s+=str(self._coefficients[i])+"x"+"+"
                else:
                    if not(self._coefficients[i]==0):
                        s+=str(self._coefficients[i])+"x"+"^({})".format(self._powers[i])+"+"
            else:
                if self._powers[i]==0 and not(self._coefficients[i]==0):
                    s+=str(self._coefficients[i])
                elif self._powers[i]==1 and not(self._coefficients[i]==0):
                    s+=str(self._coefficients[i])+"x"
                else:
                    if not(self._coefficients[i]==0):
                        s+=str(self._coefficients[i])+"x"+"^({})".format(self._powers[i])
        return s

    def subs(self,i):
        '''
        Substituition
        i : int 
        '''
        assert isinstance(i,int)
        s= 0
        for key, val in self._poly.items():
            s += val*(i**key)
        
        return s
    
    def __truediv__(self,other):
        '''
        

        Parameters
        ----------
        other : polynomial
            Division

        Raises
        ------
        NotImplementedError
            When it is not a perfect division (there is a remainder)

        Returns
        -------
        polynomial
            

        '''
        assert isinstance(self,Polynomial) and isinstance(other,Polynomial)
        if max(other._powers)>max(self._powers):
            raise NotImplementedError
        else:
            self_p=copy.deepcopy(self._powers)
            self_c=copy.deepcopy(self._coefficients)
            other_p=copy.deepcopy(other._powers)
            other_c=copy.deepcopy(other._coefficients)
            self_c=[y for x,y in sorted(zip(self_p,self_c),reverse=True)]
            other_c=[y for x,y in sorted(zip(other_p,other_c),reverse=True)]
            self_p=sorted(self_p,reverse=True)
            other_p=sorted(other_p,reverse=True)
            res_p=[]
            res_c=[]
            i=0
            while True:
                temp_c=[]
                temp_p=[]
                if i==0:
                    res_p.append(self_p[0]-other_p[0])
                    if self_c[0]%other_c[0]==0:
                        res_c.append(self_c[0]//other_c[0])
                    else:
                        raise NotImplementedError
                else:
                    next_c=[x for _,x in sorted(zip(step._powers,step._coefficients),reverse=True)]
                    next_p=sorted(step._powers,reverse=True)
                    res_p.append(next_p[0]-other_p[0])
                    if next_c[0]%other_c[0]==0:
                        res_c.append(next_c[0]//other_c[0])
                    else:
                        raise NotImplementedError
                    
                for j in range(len(other_c)):
                    temp_c.append(other_c[j]*res_c[i])
                    temp_p.append(other_p[j]+res_p[i])
        
                temp_c=[x for _,x in sorted(zip(temp_p,temp_c))]
                temp_p=sorted(temp_p)
                temp=Polynomial(dict(zip(temp_p,temp_c)))
                #print(temp)
                #print(i)
                if i==0:
                    step=self-temp
                   
                else:
                    step=step-temp
                
                
                if step==0:
                    res_c=[x for _,x in sorted(zip(res_p,res_c))]
                    resp=sorted(res_p)
                    
                    return Polynomial(dict(zip(res_p,res_c)))
                elif max(step._powers)<max(other._powers):
                    raise NotImplementedError
                i+=1

