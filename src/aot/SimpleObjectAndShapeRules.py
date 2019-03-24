
import PIL
import random

from  .KandinskyTruth    import KandinskyTruthInterfce
from  .KandinskyUniverse import kandinskyShape, overlaps



class RandomObjects (KandinskyTruthInterfce):

   def  humanDescription (self):
      return "random kandinsky figure"

   def  _randomkf(self, n):
      kf = []
      for i in range (n):
         o = kandinskyShape()
         o.color = random.choice (self.u.kandinsky_colors)
         o.shape = random.choice (self.u.kandinsky_shapes)
         o.size  = 0.1+ 0.4 * random.random ()
         o.x     = o.size/2 + random.random () * (1-o.size )
         o.y     = o.size/2 + random.random () * (1-o.size )
         kf.append (o)
      return kf

   def  true_kf (self, n=1):
      kfs = []
      for i in range (n):
         kf = self._randomkf(4)
         while overlaps (kf):
            kf = self._randomkf(4)
         kfs.append(kf)
      return kfs   


class ContainsRedObjects (KandinskyTruthInterfce):

   def  isfuzzy (self):
      return false

   def  humanDescription (self):
      return "contain at least a read object"

   def  true_kf (self, n=1):
      return []

   def  false_kf (self, n=1):
      return []


