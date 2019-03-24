import abc

class KandinskyTruthInterfce:

   def __init__(self, universe):
      # u = a kandisky univere class
      self.u = universe
      
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
