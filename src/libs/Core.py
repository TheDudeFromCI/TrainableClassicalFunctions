from Function import *
from Port import *
from ObjectType import *

AnyType = ObjectType('Any')
BooleanType = ObjectType('Boolean')
StringType = ObjectType('String')
NumberType = ObjectType('Number')

def IfFunction():
  def handler(inputs):
    return [inputs[1] if inputs[0] else inputs[2]]
  
  return Function([BooleanType, AnyType, AnyType], [AnyType], handler, 'If')

def CastToNumber():
  def handler(inputs):
    if type(inputs[0]) not in [int, float]: raise RuntimeError('Value cannot be cast to Number!')
    return [inputs[0]]

  return Function([AnyType], [NumberType], handler, 'CastToNumber')

def CastToString():
  def handler(inputs):
    if inputs[0] is not str: raise RuntimeError('Value cannot be cast to String!')
    return [inputs[0]]

  return Function([AnyType], [StringType], handler, 'CastToString')

def CastToBoolean():
  def handler(inputs):
    if inputs[0] is not bool: raise RuntimeError('Value cannot be cast to Boolean!')
    return [inputs[0]]

  return Function([AnyType], [BooleanType], handler, 'CastToBoolean')
