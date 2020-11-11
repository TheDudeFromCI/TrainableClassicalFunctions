from Port import *

class Function:
  def __init__(self, inputs, outputs, handlerFunc):
    self.inputs = [Port(self, True, 0, objType) for objType in inputs]
    self.outputs = [Port(self, False, 0, objType) for objType in outputs]
    self.handler = handlerFunc
    self.inputGroups = [[]] * len(inputs)
    self.__temp = None

    for i in range(len(self.inputs)): self.inputs[i].index = i
    for i in range(len(self.outputs)): self.outputs[i].index = i

  def run(self, inputs):
    self.__temp = self.handler(inputs)
    return self.__temp

  def clone(self):
    inputs = [p.objectType for p in self.inputs]
    outputs = [p.objectType for p in self.outputs]
    return Function(inputs, outputs, self.handler)

  def __get_port_conn(self, port):
    c = None
    for conn in self.inputGroups[port]:
      if c == None or conn.value > c.value:
        c = conn
    
    return c

  def clear_temp(self):
    self.__temp = None

  def resolve(self):
    if self.__temp != None: return self.__temp

    inputParams = []
    for port in range(len(self.inputs)):
      conn = self.__get_port_conn(port)
      result = conn.parent.function.resolve()
      inputParams.append(result[conn.parent.index])

    return self.run(inputParams)
