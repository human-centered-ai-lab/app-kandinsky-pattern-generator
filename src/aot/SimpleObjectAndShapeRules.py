
import PIL
import random

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
      randomKFgenerator = Random (self.u,self.min,self.max)
      while i<n:
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
      for kf in kfs:
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
      i = 0
      randomKFgenerator = Random (self.u,self.min,self.max)
      kfs = randomKFgenerator.true_kf(n)
      for kf in kfs:
         for s in kf:
            if s.shape == "triangle":
               s.shape = "circle"
               s.size = 0.5 * s.size 
      return kfs


