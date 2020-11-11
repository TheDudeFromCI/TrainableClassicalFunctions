class ObjectType:
  def __init__(self, name) -> None:
    self.name = name

  def can_connect_to(self, objectType):
    return self.name == objectType.name