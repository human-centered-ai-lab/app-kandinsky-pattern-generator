
import KandinskyTruth

class KandinskyFigureHasARedObject (KandinskyTruth):

   def  isfuzzy (self):
      return false

   @abc.abstractmethod
   def  true_kf (self, n=1):
      pass

   @abc.abstractmethod
   def  false_kf (self, n=1):
      pass

   @abc.abstractmethod
   def  kf (self, p, n=1):
      pass

