from Function import *
from Port import *
from ObjectType import *

NumberType = ObjectType('Number')

def AddFunction():
  def handler(inputs):
    return [inputs[0] + inputs[1]]
  
  return Function([NumberType, NumberType], [NumberType], handler)

def SubtractFunction():
  def handler(inputs):
    return [inputs[0] - inputs[1]]
  
  return Function([NumberType, NumberType], [NumberType], handler)

def MultiplyFunction():
  def handler(inputs):
    return [inputs[0] * inputs[1]]
  
  return Function([NumberType, NumberType], [NumberType], handler)

def DivideFunction():
  def handler(inputs):
    return [inputs[0] / inputs[1]]
  
  return Function([NumberType, NumberType], [NumberType], handler)

def PowerFunction():
  def handler(inputs):
    return [inputs[0] ** inputs[1]]
  
  return Function([NumberType, NumberType], [NumberType], handler)
