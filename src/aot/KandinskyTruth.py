import abc

class KandinskyTruthInterfce:

   def __init__(self, universe, min = 4, max = 4 ):
      self.u = universe
      self.min = min
      self.max = max
      
   @abc.abstractmethod
   def  humanDescription (self):
      return ""
   
   @abc.abstractmethod
   def  isfuzzy (self):
      return False

   @abc.abstractmethod
   def  true_kf (self, n=1):
      return []

   @abc.abstractmethod
   def  false_kf (self, n=1):
      return []

   @abc.abstractmethod
   def  almost_true_kf (self, n=1):
      return []
      
   @abc.abstractmethod
   def  kf (self, p, n=1):
      return []
