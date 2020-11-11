from Function import *
from ObjectType import *

class Port:
  def __init__(self, function, isInput, objectType):
    self.function = function
    self.isInput = isInput
    self.objectType = objectType
