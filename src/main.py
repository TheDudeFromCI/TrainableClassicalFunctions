from ObjectType import *
from libs.Math import *
from libs.Core import *
from Function import *
from Network import *

def build_function_list():
  return [
    AddFunction(),
    SubtractFunction(),
    MultiplyFunction(),
    DivideFunction(),
    PowerFunction(),
    IfFunction(),
    CastToNumber(),
    CastToString(),
    CastToBoolean()
  ]

if __name__ == '__main__':
  functions = build_function_list()
  inputParams = [NumberType, NumberType, BooleanType]
  outputParams = [NumberType]
  hiddenLayers = 5
  network = create_network(functions, inputParams, outputParams, hiddenLayers)

  print(convert_to_code(network))

  print(network.run([2, 4, False]))