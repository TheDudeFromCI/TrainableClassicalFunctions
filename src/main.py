from TrainingSupervisor import *
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

  trainer = TrainingSupervisor(network)
  trainer.connectionShuffle = 1.0
  trainer.learningRate = 0.05
  trainer.trainingSamples.append([[2, 4, False], [16]])

  for i in range(10000):
    trainer.do_training_itr()
    print("GENERATION " + str(i))
    print(convert_to_code(network))

    try:
      print(network.run([2, 4, False]))
    except:
      print('[Error]')