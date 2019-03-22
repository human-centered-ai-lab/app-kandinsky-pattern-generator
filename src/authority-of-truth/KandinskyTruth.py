import abc
import KandinskyUniverse

class KandinskyTruth:

   def __init__(self, universe):
      # u = a kandisky univere class
      self.u = universe
      
   @abc.abstractmethod
   def  humanDescription (self):
      pass
   
   @abc.abstractmethod
   def  isfuzzy (self):
      pass

   @abc.abstractmethod
   def  true_kf (self, n=1):
      pass

   @abc.abstractmethod
   def  false_kf (self, n=1):
      pass

   @abc.abstractmethod
   def  kf (self, p, n=1):
      pass

   def  random_kf (self, p, n=1):
      pass
