
import PIL
import random

from  .KandinskyTruth    import KandinskyTruthInterfce
from  .KandinskyUniverse import kandinskyShape, overlaps


class FixedNumber (KandinskyTruthInterfce):

   def  humanDescription (self):
      return "randfixed number (to min)"

   def __init__(self, universe, min = 4, max = 4, onlyredcircles = True ):
      self.onlyredcircles = onlyredcircles
      super().__init__(universe, min, max)
      self.max = self.min 

   def _randomobject (self, minsize = 0.1, maxsize = 0.1):
      o = kandinskyShape()
      o.color = random.choice (self.u.kandinsky_colors)
      o.shape = random.choice (self.u.kandinsky_shapes)
      o.size  = minsize +  (maxsize-minsize) * random.random ()
      o.x     = o.size/2 + random.random () * (1-o.size )
      o.y     = o.size/2 + random.random () * (1-o.size )
      return o

   def  _randomkf (self, min, max):
      kf = []
      kftemp = []
      n = random.randint (min,max)
      print ("SSS ", n)
      minsize = 0.1      
      maxsize = 0.1
      i = 0
      maxtry= 20
      while i<n:
         kftemp = kf
         t = 0
         o = self._randomobject(minsize, maxsize)
         kftemp = kf[:]
         kftemp.append (o)
         while overlaps (kftemp) and (t < maxtry):
            o = self._randomobject(minsize, maxsize)
            kftemp = kf[:]
            kftemp.append (o)
            t = t + 1
         if (t < maxtry):
            kf = kftemp[:]
            i = i + 1
         else: 
            maxsize = maxsize*0.95   
            minsize = minsize*0.95   
      return kf

   def  true_kf (self, n=1):
      kfs = []
      for i in range (n):
         kf = self._randomkf(self.min, self.max)
         if self.onlyredcircles:
            for s in kf:
               s.shape = 'circle'
               s.color = 'red'
         kfs.append(kf)
      return kfs   
  
   def  almost_true_kf (self, n=1):
     
      deltamin = self.min  - 1
      deltamax = 2 * self.max 
      minToMax = deltamin / deltamax
      kfs = []    
      for i in range (n):
         if (random.random () < minToMax):
            # if min == 1 we neve come to this code
            minmin = max (1, self.min - 2)
            numberOfElementsMin = random.randint (minmin, self.min - 1)
            numberOfElementsMax = self.min - 1
         else:
            numberOfElementsMin = self.max + 1
            numberOfElementsMax = self.max + 2
    
         kf = self._randomkf(numberOfElementsMin, numberOfElementsMax)
         if self.onlyredcircles:
            for s in kf:
               s.shape = 'circle'
               s.color = 'red'
         kfs.append(kf)
      return kfs

   def  false_kf (self, n=1):
      kfs = []
      deltamin = self.min  - 1
      deltamax = 2 * self.max 
      minToMax = deltamin / deltamax

      kfs = []
      for i in range (n):
         if (random.random () <   minToMax):
         # if min == 1 we neve come to this code
            numberOfElementsMin = 1
            numberOfElementsMax = self.min - 1
         else:
            numberOfElementsMin = self.max + 1
            numberOfElementsMax = 2 * self.max

         print (numberOfElementsMin, numberOfElementsMax)
         
      
         kf = self._randomkf(numberOfElementsMin, numberOfElementsMax)
         if self.onlyredcircles:
            for s in kf:
               s.shape = 'circle'
               s.color = 'red'
         kfs.append(kf)
      return kfs