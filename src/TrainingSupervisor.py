from random import randrange, random

class TrainingSupervisor:
  def __init__(self, network):
    self.network = network
    self.connectionShuffle = 0.5
    self.learningRate = 0.3
    self.trainingSamples = []
    self.antipatterns = []
    self.errorCost = 1

  def next_sample(self):
    return self.trainingSamples[randrange(0, len(self.trainingSamples))]

  def get_error_distance(self):
    return self.errorCost * self.learningRate
  
  def get_distance(self, result, answer):
    if self.network_has_antipatterns(): return self.get_error_distance()

    # TODO Make smoother gradient by doing actual type checking

    distance = 0
    for i in range(len(answer)):
      if result[i] != answer[1]: distance += 1
    distance /= len(answer)

    return (distance + self.get_performance_cost()) * self.learningRate

  def get_performance_cost(self):
    # TODO Read network and determine performance cost
    return 0
  
  def network_has_antipatterns(self):
    # TODO Check if network has antipatterns
    return False

  def do_training_itr(self):
    def set_delta(conn):
      lerp = self.connectionShuffle
      delta = random() * lerp + conn.weight * (1 - lerp)
      conn.delta = delta - conn.weight

    for conn in self.network.connections: set_delta(conn)

    dataSample = self.next_sample()
    try:
      result = self.run(dataSample[0])
      distance = self.get_distance(result, dataSample[1])
    except:
      distance = self.get_error_distance()

    if distance == 0:
      distance -= self.learningRate * 5

    self.punish_agent(distance)

    for conn in self.network.connections: conn.delta = 0

  def punish_agent(self, value):
    finishedFunctions = []
    def punish_function(func):
      if func in finishedFunctions: return
      finishedFunctions.append(func)

      for port in range(len(func.inputs)):
        conn = func.get_port_conn(port)

        if value > 0:
          conn.remove_weight(value)
        elif value < 0:
          conn.add_weight(-value)

        punish_function(conn.parent.function)

    punish_function(self.network.output)