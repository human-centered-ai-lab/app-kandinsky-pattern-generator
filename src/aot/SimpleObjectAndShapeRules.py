
from  aot.KandinskyTruth import KandinskyTruthInterfce

class ContainsRedObjects (KandinskyTruthInterfce):

   def  isfuzzy (self):
      return false

   def  humanDescription (self):
      return "contain at least a read object"

   def  true_kf (self, n=1):
      return []

   def  false_kf (self, n=1):
      return []


