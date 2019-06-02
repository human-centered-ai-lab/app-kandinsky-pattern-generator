
import PIL
import random
import math
from collections import defaultdict

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

class twoPairsOnlyOneWithSameColor (KandinskyTruthInterfce):

   def  isfuzzy (self):
      return false

   def  humanDescription (self):
      return "contains two pairs of objects with the same shape, oene with equal color, one with different color"

   def _gt (self, kf):
       
       ns   = defaultdict(dict)
       ncs  = defaultdict(dict)
   
       for s in self.u.kandinsky_shapes: 
            ns[s] = 0    
            for c in self.u.kandinsky_colors: 
                ncs[s][c] = 0     

       for s in kf: 
            ncs[s.shape][s.color] = ncs[s.shape][s.color] + 1
            ns[s.shape] = ns[s.shape] + 1   
       
       pairs = 0
       quads = 0
       p1 = ""
       p2 = ""
       for s in self.u.kandinsky_shapes: 
          if  ns[s] == 2: 
             pairs = pairs  + 1
             if p1 == "":
                p1 = s
             else:
                p2 = s

       for s in self.u.kandinsky_shapes: 
          if  ns[s] == 4:
             quads = 1
             p1 = s

       is_valid = False
       if pairs==2:
            n_of_same_cols = 0   
            for c in self.u.kandinsky_colors: 
               if ncs[p1][c] == 2:
                  n_of_same_cols = n_of_same_cols + 1
            for c in self.u.kandinsky_colors: 
               if ncs[p2][c] == 2:
                  n_of_same_cols = n_of_same_cols + 1
            if n_of_same_cols == 1:
               is_valid = True
                      
       if quads==1: 
          # print ("QUADS")
          n_of_colors = 0
          for c in self.u.kandinsky_colors: 
               if ncs[p1][c] > 0:
                  n_of_colors = n_of_colors + 1 
          if (n_of_colors == 3) or (n_of_colors == 2):
              # only if we have 2 or 3 different colors we can have two pairs not with the same colors .....
              is_valid = True  

       return is_valid



   def  true_kf (self, n=1):
      kfs = []
      i = 0
      randomKFgenerator = Random (self.u, 4,4)
      while i<n:
         kf = randomKFgenerator.true_kf(1)[0]
         if self._gt (kf):
            kfs.append (kf)
            i = i + 1
            print ("true - ", i)
      return kfs


   def  false_kf (self, n=1):
      kfs = []
      i = 0
      randomKFgenerator = Random (self.u,4,4)
      while i<n:
         kf = randomKFgenerator.true_kf(1)[0]
         if not self._gt (kf):
            kfs.append (kf)
            i = i + 1
            print ("false - ", i)
      return kfs

