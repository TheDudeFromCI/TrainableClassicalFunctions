from ObjectType import *
from libs.Math import *
from Function import *
from Network import *

def build_function_list():
  return [
    AddFunction(),
    SubtractFunction(),
    MultiplyFunction(),
    DivideFunction(),
    PowerFunction(),
  ]

if __name__ == '__main__':
  functions = build_function_list()
  inputParams = [NumberType, NumberType]
  outputParams = [NumberType]
  hiddenLayers = 5
  network = create_network(functions, inputParams, outputParams, hiddenLayers)

  print(network.run([2, 4]))