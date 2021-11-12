class Interval(object):
     def __init__(self,a,b):
         """
         :a: integer
         :b: integer
         """
         assert a<b
         assert isinstance(a,int)
         assert isinstance(b,int)
         self._a = a
         self._b = b
     
     def __repr__(self):
         '''
         

         Returns
         -------
         a : string
             returns the onject or list of objects in the form

         '''
         a = "Interval(" + str(self._a) + "," + str(self._b) + ")"
         return a
         
         
     def __eq__(self,other):
        '''       

         Parameters
         ----------
         other : Interval object
             the second variable to be compared for equality

         Returns
         -------
         bool
             returns true if the both the limits of the object are equal

         '''
        assert isinstance(self,Interval) and isinstance(other,Interval)
        return self._a==other._a and self._b==other._b
    
     def __add__(self,other):
         assert isinstance(self, Interval) 
         assert isinstance(other, Interval)
         common_numbers = set(range(self._a, self._b)).intersection(set(range(other._a, other._b)))
         if len(common_numbers) > 0:
             return Interval(min(self._a, other._a), max(self._b, other._b))
         else:
             return [self, other]
         
     
