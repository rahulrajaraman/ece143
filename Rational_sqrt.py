from __future__ import division
from fractions import Fraction
import math

class Rational:
    def __init__(self, num, den):
        '''
        Parameters
        ----------
        num : int/float
            numerator
        den : int/float
            Denomenator

        Returns
        -------
        Rational object

        '''
        
        assert isinstance(num,int) and isinstance(den,int)
        assert not den == 0      
        self._num = num
        self._den = den
        
    
    def __add__(self, other):
        '''
        Parameters
        ----------
        other : Rational object
            

        Returns
        -------
        Raitonal object
            sum of two fractions.
        '''
        return Rational(self._num*other._den + self._den*other._num, self._den*other._den)
    
    def __sub__(self,other):
        '''
        

        Parameters
        ----------
        other : Rational
            

        Returns
        -------
        Rational
        

        '''
        return Rational(self._num*other._den - self._den*other._num, self._den*other._den)
    
    def __radd__(self,other):
        '''
        Addition for other classes
        '''
        assert isinstance(self,Rational)
        return Rational(self._num+other*self._den,self._den)
    
    def __float__(self):
        '''
        Converts onject to float value
        '''
        assert isinstance(self,Rational)
        return self._num/self._den
    
    def __mul__(self,other):
        '''
        

        Parameters
        ----------
        other : Rational
            

        Returns
        -------
        result : Rational
            
        Multiplication function

        '''
        result=Rational(1,1)
        if isinstance(other,Rational):
            result._num=self._num*other._num
            result._den=self._den*other._den
        else:
            result._num=self._num*other
            result._den=self._den
        return result

    def __neg__(self):
        '''
        

        Returns
        -------
        Rational
            -1*R

        '''
        assert isinstance(self, Rational)
        if self._num/self._den == int(self._num/self._den):
            return Rational(-1*int(self._num/self._den),1)
        else:
            return Rational(-1*self._num,self._den)

    def __int__(self):
        '''
        

        Returns
        -------
        Raitonal
            

        '''
        
        return int(self._num/self._den)
    
    def __repr__(self):
        '''
        printing method
        '''
        assert isinstance(self,Rational)
        if (self._num/self._den)==int(self._num/self._den):
            return '{}'.format(int(self._num/self._den))
        else:
            return '{}/{}'.format(self._num,self._den)
    
    
    def __eq__(self,other):
        '''
        Check if self == other
        '''
        assert isinstance(self,Rational)
        if isinstance(other,Rational):
            if (self._num/self._den)==(other._num/other._den):
                return True
            else:
                return False
        else:
            if (self._num/self._den)==other:
                return True
            else:
                return False
    
    def __truediv__(self,other):
        '''
        

        Parameters
        ----------
        other : Any class
            can be of any class (int float etc)

        Returns
        -------
        res : Rational
            

        '''
        assert isinstance(self,Rational)
        
        res=Rational(1,1)
        if isinstance(other,Rational):
            res._num=self._num*other._den
            res._den=self._den*other._num
        else:
            res._num=self._num
            res._den=self._den*other
        return res
    
    def __rtruediv__(self,other):
        '''
        Used when other is of different class
        '''
        return Rational(Fraction(other*self._den/self._num).limit_denominator().numerator,Fraction(other*self._den/self._num).limit_denominator().denominator)
    
    
    def __lt__(self,other):
        '''
        less than
        '''
        assert isinstance(other,Rational)
        assert isinstance(self,Rational)
        if (self._num/self._den)<(other._num/other._den):
            return True
        else:
            return False
        
    def __gt__(self,other):
        '''
        greater than
        '''
        assert isinstance(other,Rational)
        assert isinstance(self,Rational)
        
        if (self._num/self._den)>(other._num/other._den):
            return True
        else:
            return False
    def __le__(self,other):
        '''
        less equals
        '''
        assert isinstance(other,Rational)
        assert isinstance(self,Rational)
        
        if (self._num/self._den)<=(other._num/other._den):
            return True
        else:
            return False
    def __ge__(self,other):
        '''
        greater equals
        '''
        assert isinstance(other,Rational)
        assert isinstance(self,Rational)
        
        if (self._num/self._den)>=(other._num/other._den):
            return True
        else:
            return False
    
    def sorted(x):
        '''
        Sorting func

        Parameters
        ----------
        x : list
            list of Rationals

        Returns
        -------
        res : list
            list of sorted Rationals

        '''
        assert isinstance(x,list)
        for i in x:
            assert isinstance(i,Rational)
        res=[]
        while x:
            minimum = x[0]._num/x[0]._den
            print(minimum)
            min_index=0
            for i in range(len(x)): 
                if (x[i]._num/x[i]._den) < minimum:
                    minimum = x[i]
                    min_index=i
            res.append(x[min_index])
            x.remove(x[min_index])
        return res


def square_root_rational(x, abs_tol = Rational(1,1000)):
    '''
    

    Parameters
    ----------
    x : Rational 
        Rational num
    abs_tol : Rational, optional
        tolerance value. The default is Rational(1,1000).

    Returns
    -------
    Rational object

    '''
    assert isinstance(x,Rational) and isinstance(abs_tol, Rational)
    ub = float(x)
    lb = float(Rational(0,1))
    m = Rational(1,1)
    while True:
        m = (ub+lb)/2
        if abs(float(m)-math.sqrt(x))<=float(abs_tol):
            return Rational(Fraction(m).limit_denominator().numerator,Fraction(m).limit_denominator().denominator)
        else:
            if float(x)>float(m)**2:
                lb = m
            else:
                ub = m

