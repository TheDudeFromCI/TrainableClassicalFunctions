from ObjectType import *
from libs.Math import *
from Function import *
from Network import *

def InputFunction():
  def handler(inputs):
    return inputs
  
  return Function([], [NumberType, NumberType], handler)

def OutputFunction():
  def handler(inputs):
    return inputs

  return Function([NumberType], [], handler)

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
  network = create_network(functions, InputFunction(), OutputFunction(), 5)

  print(len(network.connections))