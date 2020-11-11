from Connection import *
from random import random

class Network:
  def __init__(self, connections, inputFunc, outputFunc):
    self.connections = connections
    self.input = inputFunc
    self.output = outputFunc

  def run(self, inputs):
    pass

  def randomize_connection_delta(self):
    pass

def create_network(functions, inputFunc, outputFunc, hiddenLayers):
  connections = []

  # Build layer map
  layers = []
  layers.append([inputFunc.clone()])
  for _ in range(hiddenLayers):
    layer = []
    for func in functions: layer.append(func.clone())
    layers.append(layer)
  layers.append([outputFunc.clone()])

  # Unify function list
  realFuncList = []
  for layer in layers: realFuncList.extend(layer)

  # Initialize all connections
  for layerIndex in range(len(layers)):
    for outputFunc in layers[layerIndex]:
      for outputPort in outputFunc.outputs:
        for futureLayerIndex in range(layerIndex + 1, len(layers)):
          for inputFunc in layers[futureLayerIndex]:
            for inputPort in inputFunc.inputs:
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
  
  # Create the network
  return Network(connections, inputFunc, outputFunc)