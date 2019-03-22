
import KandinskyTruth

class ContainsARedObjects (KandinskyTruth):

   def  isfuzzy (self):
      return false

   def  humanDescription (self):
      return "contains at least a read object"

   @abc.abstractmethod
   def  true_kf (self, n=1):
      pass

   @abc.abstractmethod
   def  false_kf (self, n=1):
      pass

   @abc.abstractmethod
   def  kf (self, p, n=1):
      return []

