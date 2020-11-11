from Port import *

class Function:
  def __init__(self, inputs, outputs, handlerFunc):
    self.inputs = [Port(self, True, objType) for objType in inputs]
    self.outputs = [Port(self, False, objType) for objType in outputs]
    self.handler = handlerFunc

  def run(self, inputs):
    return self.handler(inputs)

  def clone(self):
    inputs = [p.objectType for p in self.inputs]
    outputs = [p.objectType for p in self.outputs]
    return Function(inputs, outputs, self.handler)