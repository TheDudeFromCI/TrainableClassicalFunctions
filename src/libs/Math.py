from Function import *
from Port import *
from ObjectType import *

NumberType = ObjectType('Number')

def AddFunction():
  def handler(inputs):
    return [inputs[0] + inputs[1]]
  
  return Function([NumberType, NumberType], [NumberType], handler, 'Add')

def SubtractFunction():
  def handler(inputs):
    return [inputs[0] - inputs[1]]
  
  return Function([NumberType, NumberType], [NumberType], handler, 'Subtract')

def MultiplyFunction():
  def handler(inputs):
    return [inputs[0] * inputs[1]]
  
  return Function([NumberType, NumberType], [NumberType], handler, 'Multiply')

def DivideFunction():
  def handler(inputs):
    return [inputs[0] / inputs[1]]
  
  return Function([NumberType, NumberType], [NumberType], handler, 'Divide')

def PowerFunction():
  def handler(inputs):
    return [inputs[0] ** inputs[1]]
  
  return Function([NumberType, NumberType], [NumberType], handler, 'Power')
