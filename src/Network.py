from Connection import *
from Function import *
from random import random

class Network:
  def __init__(self, connections, functionList, inputFunc, outputFunc):
    self.connections = connections
    self.functionList = functionList
    self.input = inputFunc
    self.output = outputFunc

  def run(self, inputs):
    self.input.run(inputs)
    result = self.output.resolve()

    for func in self.functionList: func.clear_temp()

    return result

  def randomize_connection_delta(self):
    pass

def create_network(functions, inputParams, outputParams, hiddenLayers):
  connections = []

  inputFunc = Function([], inputParams, lambda inputs: inputs, 'Input')
  outputFunc = Function(outputParams, [], lambda inputs: inputs, 'Output')

  # Build layer map
  layers = []
  layers.append([inputFunc])
  for _ in range(hiddenLayers):
    layer = []
    for func in functions: layer.append(func.clone())
    layers.append(layer)
  layers.append([outputFunc])

  # Unify function list
  realFuncList = []
  for layer in layers: realFuncList.extend(layer)

  # Initialize all connections
  for layerIndex in range(len(layers)):
    for outputF in layers[layerIndex]:
      for outputPort in outputF.outputs:
        for futureLayerIndex in range(layerIndex + 1, len(layers)):
          for inputF in layers[futureLayerIndex]:
            for inputPort in inputF.inputs:
              if not outputPort.objectType.can_connect_to(inputPort.objectType): continue
              conn = Connection(outputPort, inputPort)
              conn.weight = random()
              connections.append(conn)
  
  # Trim unusable functions from the list
  def has_inputs(func):
    unsatisfiedInputs = len(func.inputs)
    if unsatisfiedInputs == 0: return True

    for input in func.inputs:
      for conn in connections:
        if conn.child is input:
          unsatisfiedInputs -= 1
          break

    return unsatisfiedInputs == 0

  def has_outputs(func):
    if len(func.outputs) == 0: return True

    for output in func.outputs:
      for conn in connections:
        if conn.parent is output:
          return True

    return False

  def conn_references_func(conn, func):
    for input in func.inputs:
      if input is conn.child: return True

    for output in func.outputs:
      if output is conn.parent: return True

    return False

  # Remove all functions that fail to meet input/output requirements
  # Since removing a function can break more functions, repeat until
  # no more changes are made to the function list.
  while True:
    toRemove = []
    for func in realFuncList:
      if has_inputs(func) and has_outputs(func): continue

      # Function cannot exist here
      toRemove.append(func)
      connections = [c for c in connections if not conn_references_func(c, func)]

    if len(toRemove) == 0: break
    realFuncList = [f for f in realFuncList if f not in toRemove]
  
  # Group connections as siblings
  for conn in connections:
    for pair in connections:
      if conn.child is not pair.child: continue
      conn.siblings.append(pair)
    
    conn.normalize_weights()
    conn.child.function.inputGroups[conn.child.index] = conn.siblings
  
  # Create the network
  return Network(connections, realFuncList, inputFunc, outputFunc)

def convert_to_code(network):

  varIndex = 0

  class CodeVar:
    def __init__(self, parentPort, index):
      self.parentPort = parentPort
      self.index = index

    def __str__(self):
      return 'v' + str(self.index)

  class CodeLine:
    def __init__(self, function):
      nonlocal varIndex

      self.function = function
      self.inputVars = []
      self.outputVars = []
      self.indent = 1

      for output in function.outputs:
        self.outputVars.append(CodeVar(output, varIndex))
        varIndex += 1

    def __str__(self):

      if self.function is network.input:
        line = 'function('
        line += ', '.join(str(v) for v in self.outputVars)
        line += '):'
        return line

      line = '  ' * self.indent

      if self.function is network.output:
        line += 'return '
        line += ', '.join(str(v) for v in self.inputVars)
      else:
        if len(self.outputVars) > 0:
          line += ', '.join(str(v) for v in self.outputVars) + ' = '

        line += self.function.name
        line += '('
        line += ', '.join(str(v) for v in self.inputVars)
        line += ')'

      return line

  lines = []
  def build_lines(func):
    line = None
    for l in lines:
      if l.function is func:
        line = l
        break

    if line != None: return line

    line = CodeLine(func)
    lines.append(line)

    for port in range(len(func.inputs)):
      conn = func.get_port_conn(port)
      parentFunc = build_lines(conn.parent.function)

      line.inputVars.append(parentFunc.outputVars[conn.parent.index])
    
    return line

  build_lines(network.output)

  def is_too_high(line):
    index = lines.index(line)
    for i in range(index + 1, len(lines)):
      for input in line.inputVars:
        for output in lines[i].outputVars:
          if input is output: return True
    
    return False

  def push_to_end(line):
    lines.remove(line)
    lines.append(line)

  while True:
    edited = False
    for i in range(len(lines)):
      line = lines[i]
      if is_too_high(line):
        push_to_end(line)
        edited = True
        break

    if not edited: break

  code = ''
  for line in lines: code += str(line) + '\n'
  return code