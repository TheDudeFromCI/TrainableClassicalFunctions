from Function import *
from ObjectType import *

class Port:
  def __init__(self, function, isInput, index, objectType):
    self.function = function
    self.isInput = isInput
    self.index = index
    self.objectType = objectType
