
import PIL
import random
import math

from  .KandinskyTruth    import KandinskyTruthInterfce
from  .KandinskyUniverse import kandinskyShape, overlaps
from  .RandomKandinskyFigure import Random

class ContainsRedObjects (KandinskyTruthInterfce):
   
   def  isfuzzy (self):
      return false

   def  humanDescription (self):
      return "contain at least a red object"

   def  true_kf (self, n=1):
      kfs = []
      i = 0
      print ("MAKE TRUE")
      randomKFgenerator = Random (self.u,self.min,self.max)
      while i<n:
         print (i)
         kf = randomKFgenerator.true_kf(1)[0]
         hasRed = False
         for s in kf:
            if s.color == "red":
               hasRed = True   
         if hasRed:
            kfs.append (kf)
            i = i + 1
      return kfs

   def  false_kf (self, n=1):
      kfs = []
      i = 0
      randomKFgenerator = Random (self.u,self.min,self.max)
      kfs = randomKFgenerator.true_kf(n)
      print ("MAKE FALSE")
      for kf in kfs:
         print (i)

         for s in kf:
            if s.color == "red":
               s.color = "blue"
      return kfs


class ContainsTriangles (KandinskyTruthInterfce):

   def  isfuzzy (self):
      return false

   def  humanDescription (self):
      return "contain at least a triangle object"

   def  true_kf (self, n=1):
      kfs = []
      i = 0
      randomKFgenerator = Random (self.u,self.min,self.max)
      while i<n:
         kf = randomKFgenerator.true_kf(1)[0]
         hasT = False
         for s in kf:
            if s.shape == "triangle":
               hasT = True   
         if hasT:
            kfs.append (kf)
            i = i + 1
      return kfs

   def  false_kf (self, n=1):
      kfs = []
      randomKFgenerator = Random (self.u,self.min,self.max)
      kfs = randomKFgenerator.true_kf(n)
      for kf in kfs:
         for s in kf:
            if s.shape == "triangle":
               s.shape = "circle"
               s.size = 0.5 * s.size 
      return kfs

class Cells (KandinskyTruthInterfce):

   def _cell (self):
      o = kandinskyShape()
      o.color = random.choice (["blue", "yellow"])
      o.shape = "circle"
      o.size  = 32.0 * math.pi / 512 / 0.7 / 4
      o.x     = o.size/2 + random.random () * (1-o.size )
      o.y     = o.size/2 + random.random () * (1-o.size )
      return o

   def _cells (self, n):
      kf = []
      maxtry = 10
      i = 0
      while i<n:
         kftemp = kf
         t = 0
         o = self._cell()
         kftemp = kf[:]
         kftemp.append (o)
         while overlaps (kftemp) and (t < maxtry):
            o = self._cell()
            kftemp = kf[:]
            kftemp.append (o)
            t = t + 1
         if (t < maxtry):
            kf = kftemp[:]
         i = i + 1   
      return kf


   def  isfuzzy (self):
      return false

   def  humanDescription (self):
      return "circles representing two cell types"

   def  true_kf (self, n=1):

      kfs = []
      i = 0
      while i<n:
         print (i)
         kfs.append (self._cells(100))
         i = i + 1
      return kfs

   def  false_kf (self, n=1):
      kfs = []
      return kfs
