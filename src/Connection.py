from Port import *

class Connection:
  def __init__(self, parent, child):
    self.parent = parent
    self.child = child
    self.weight = 1
    self.delta = 0
    self.siblings = []

  def normalize_weights(self):
    total = 0
    for sib in self.siblings: total += sib.weight
    for sib in self.siblings: sib.weight /= total
  
  def add_weight(self, value):
    if len(self.siblings) == 1: return
    self.weight += value
    self.normalize_weights()
  
  def remove_weight(self, value):
    if len(self.siblings) == 1: return
    value /= len(self.siblings) - 1
    for sib in self.siblings:
      if sib is self: continue
      sib.weight += value
    
    self.normalize_weights()

  @property
  def value(self):
    return self.weight + self.delta