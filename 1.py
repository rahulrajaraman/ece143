from __future__ import division
import copy

class Polynomial(object):
    '''This class performs operations on polynomials'''
    def __init__(self,input_dict):
        assert isinstance(input_dict,dict)
        self._powers=list(input_dict.keys())
        self._coefficients=list(input_dict.values())
        self._coefficients=[x for _,x in sorted(zip(self._powers,self._coefficients))]
        self._powers=sorted(self._powers)
        for i in self._powers:
            assert isinstance(i,int)
        for i in self._coefficients:
            assert isinstance(i,int)
    def __repr__(self):
        res=""
        assert isinstance(self,Polynomial)
        for i in range(len(self._powers)):
            if not(i==len(self._powers)-1):
                if self._powers[i]==0 and not(self._coefficients[i]==0):
                    res+=str(self._coefficients[i])+"+"
                elif self._powers[i]==1 and not(self._coefficients[i]==0):
                    res+=str(self._coefficients[i])+"x"+"+"
                else:
                    if not(self._coefficients[i]==0):
                        res+=str(self._coefficients[i])+"x"+"^({})".format(self._powers[i])+"+"
            else:
                if self._powers[i]==0 and not(self._coefficients[i]==0):
                    res+=str(self._coefficients[i])
                elif self._powers[i]==1 and not(self._coefficients[i]==0):
                    res+=str(self._coefficients[i])+"x"
                else:
                    if not(self._coefficients[i]==0):
                        res+=str(self._coefficients[i])+"x"+"^({})".format(self._powers[i])
        return res

    def __mul__(self,other):
        assert isinstance(self,Polynomial)
        assert isinstance(other,int) or isinstance(other,Polynomial)
        if isinstance(other,int):
            coeffs=copy.deepcopy(self._coefficients)
            for i in range(len(coeffs)):
                coeffs[i]*=other
            res_dict=dict(zip(self._powers,coeffs))
            if all([v==0 for v in coeffs]):
                res=Polynomial(res_dict)
                return res
            to_remove=[]
            for key in res_dict:
                if res_dict[key]==0:
                    to_remove.append(key)
            for i in to_remove:
                    del res_dict[i]
            res=Polynomial(res_dict)
            return res
        else:
            powers_list=[]
            for i in range(len(self._powers)):
                for j in range(len(other._powers)):
                    powers_list.append(self._powers[i]+other._powers[j])
            res_dict=dict(zip(list(set(powers_list)),[0]*len(list(set(powers_list)))))
            #print(list(set(powers_list)))
            for i in range(len(self._coefficients)):
                for j in range(len(other._coefficients)):
                    res_dict[self._powers[i]+other._powers[j]]+=self._coefficients[i]*other._coefficients[j]
            if all([v==0 for v in res_dict.values()]):
                res=Polynomial(res_dict)
                return res
            to_remove=[]
            for key in res_dict:
                if res_dict[key]==0:
                    to_remove.append(key)
            for i in to_remove:
                    del res_dict[i]
            res=Polynomial(res_dict)   
            return res
                          
            
    def __rmul__(self,other):
        assert isinstance(self,Polynomial) and isinstance(other,int)
        coeffs=copy.deepcopy(self._coefficients)
        for i in range(len(coeffs)):
            coeffs[i]*=other
        res_dict=dict(zip(self._powers,coeffs))
        if all([v==0 for v in coeffs]):
            return Polynomial(res_dict)
        to_remove=[]
        for key in res_dict:
            if res_dict[key]==0:
                to_remove.append(key)
        for i in to_remove:
            del res_dict[i]
        res=Polynomial(res_dict)
        return res
    def __add__(self,other):
        assert isinstance(self,Polynomial)
        assert isinstance(other,Polynomial) or isinstance(other,int)
        if isinstance(other,Polynomial):
            powers=list(set(self._powers+other._powers))
        else:
            powers=self._powers
        input_dict=dict(zip(powers,[0]*len(powers)))
        for i in range(len(self._powers)):
            input_dict[self._powers[i]]+=self._coefficients[i]
        if isinstance(other,Polynomial):
            for i in range(len(other._powers)):
                input_dict[other._powers[i]]+=other._coefficients[i]
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
        else:
            input_dict[0]+=other
            res=Polynomial(input_dict)
            return res
    def __radd__(self,other):
        assert isinstance(self,Polynomial) and isinstance(other,int)
        powers=self._powers
        input_dict=dict(zip(powers,[0]*len(powers)))
        for i in range(len(self._powers)):
            input_dict[self._powers[i]]+=self._coefficients[i]
        input_dict[0]+=other
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
    
    def __sub__(self,other):
        assert isinstance(self,Polynomial)
        assert isinstance(other,Polynomial) or isinstance(other,int)
        if isinstance(other,Polynomial):
            other_copy=copy.deepcopy(other)
            for i in range(len(other_copy._coefficients)):
                other_copy._coefficients[i]=-1*other_copy._coefficients[i]
            powers=list(set(self._powers+other_copy._powers))
            input_dict=dict(zip(powers,[0]*len(powers)))
            for i in range(len(self._powers)):
                input_dict[self._powers[i]]+=self._coefficients[i]
            for i in range(len(other_copy._powers)):
                input_dict[other_copy._powers[i]]+=other_copy._coefficients[i]
            if all([v==0 for v in input_dict.values()]):
                #print(list(input_dict.values()))
                #print("Hi")
                return Polynomial(input_dict)
            to_remove=[]
            for key in input_dict:
                if input_dict[key]==0:
                    to_remove.append(key)
            for i in to_remove:
                    del input_dict[i]
            #print("Here")
            res=Polynomial(input_dict)
            return res
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
        assert isinstance(self,Polynomial) and isinstance(other,int)
        powers=self._powers
        input_dict=dict(zip(powers,[0]*len(powers)))
        for i in range(len(self._powers)):
            input_dict[self._powers[i]]+=self._coefficients[i]
        input_dict[0]=other-input_dict[0]
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
        
            
    def __eq__(self,other):
        assert isinstance(self,Polynomial)
        assert isinstance(other,Polynomial) or isinstance(other,int)
        if isinstance(other,Polynomial):
            if self._powers==other._powers and self._coefficients==other._coefficients:
                return True
            else:
                return False
        else:
            if all(self._coefficients)==0:
                return True
            else:
                return False
            #x=copy.deepcopy(self._powers)
            #x.remove(0)
            #for i in x:
                #assert self._coefficients[self._powers.index(i)]==0
            #if self._coefficients[0]==other:
             #   return True
            #else:
             #   return False
    def subs(self,x):
        assert isinstance(x,int)
        res=0
        for i in range(len(self._powers)):
            if self._powers[i]==0:
                res+=self._coefficients[i]
            else:
                res+=self._coefficients[i]*(x**(self._powers[i]))
        return res

    def __truediv__(self,other):
        assert isinstance(self,Polynomial) and isinstance(other,Polynomial)
        if max(other._powers)>max(self._powers):
            raise NotImplementedError
        else:
            selfp=copy.deepcopy(self._powers)
            selfc=copy.deepcopy(self._coefficients)
            otherp=copy.deepcopy(other._powers)
            otherc=copy.deepcopy(other._coefficients)
            selfc=[x for _,x in sorted(zip(selfp,selfc),reverse=True)]
            otherc=[x for _,x in sorted(zip(otherp,otherc),reverse=True)]
            selfp=sorted(selfp,reverse=True)
            otherp=sorted(otherp,reverse=True)
            resp=[]
            resc=[]
            i=0
            while True:
                tempc=[]
                tempp=[]
                if i==0:
                    resp.append(selfp[0]-otherp[0])
                    #if (selfc[i]//otherc[0])==(selfc[i]/otherc[0]):
                    if selfc[0]%otherc[0]==0:
                        resc.append(selfc[0]//otherc[0])
                    else:
                        raise NotImplementedError
                else:
                    stepc=[x for _,x in sorted(zip(step._powers,step._coefficients),reverse=True)]
                    stepp=sorted(step._powers,reverse=True)
                    resp.append(stepp[0]-otherp[0])
                    #if (stepc[0]//otherc[0])==(stepc[0]/otherc[0]):
                    if stepc[0]%otherc[0]==0:
                        resc.append(stepc[0]//otherc[0])
                    else:
                        raise NotImplementedError
                    
                for j in range(len(otherc)):
                    tempc.append(otherc[j]*resc[i])
                    tempp.append(otherp[j]+resp[i])
        
                tempc=[x for _,x in sorted(zip(tempp,tempc))]
                tempp=sorted(tempp)
                temp=Polynomial(dict(zip(tempp,tempc)))
                #print(repr(temp))
                if i==0:
                    step=self-temp
                    #print('step= ',step)
                    #print(step._powers)
                    #print(step._coefficients)
                    #print(step==0)
                else:
                    step=step-temp
                #print(repr(step))
                if step==0:
                    resc=[x for _,x in sorted(zip(resp,resc))]
                    resp=sorted(resp)
                    #print(resp,resc)
                    return Polynomial(dict(zip(resp,resc)))
                elif max(step._powers)<max(other._powers):
                    raise NotImplementedError
                i+=1
                

p = Polynomial({2:1,0:-1})
q = Polynomial({1:1,0:-1})
#print(p-q)
print('soln:',p/q)