
import PIL
import random

from  .KandinskyTruth    import KandinskyTruthInterfce
from  .KandinskyUniverse import kandinskyShape, overlaps


class Random (KandinskyTruthInterfce):

   def  humanDescription (self):
      return "random kandinsky figure"

   def _randomobject (self, minsize = 0.1, maxsize = 0.5):
      o = kandinskyShape()
      o.color = random.choice (self.u.kandinsky_colors)
      o.shape = random.choice (self.u.kandinsky_shapes)
      o.size  = minsize +  (maxsize-minsize) * random.random ()
      o.x     = o.size/2 + random.random () * (1-o.size )
      o.y     = o.size/2 + random.random () * (1-o.size )
      return o

   def  _randomkf(self, min, max):
      kf = []
      kftemp = []
      n = random.randint (min,max)

      minsize = 0.1
      if n == 3: minsize = 0.2
      if n == 2: minsize = 0.3
      if n == 1: minsize = 0.4
      
      maxsize = 0.6
      if n == 5: maxsize = 0.5
      if n == 6: maxsize = 0.4
      if n == 7: maxsize = 0.3
      if n > 7: 
         m = n-7
         maxsize = 0.2 - m * (0.2)/70.0 

      if maxsize < 0.04: maxsize =  0.04
      if minsize > maxsize: minsize =  maxsize
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
         kfs.append(kf)
      return kfs   
