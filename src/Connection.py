from Port import *

class Connection:
  def __init__(self, parent, child):
    self.parent = parent
    self.child = child
    self.weight = 0
    self.delta = 0
    self.siblings = []

  def normalize_weights(self):
    total = 0
    for sib in self.siblings: total += sib.weight
    for sib in self.siblings: sib.weight /= total
  
  def add_weight(self, value):
    self.weight += value
    self.normalize_weights()
  
  def removeWeight(self, value):
    value /= len(self.siblings) - 1
    for sib in self.siblings:
      if sib is self: continue
      sib.weight += value
    
    self.normalize_weights()