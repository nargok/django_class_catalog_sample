class BroadcastViewModel(object):
  def __init__(self, broadcast, length=1000):
    self.broadcast = broadcast
    self.length = length

  @property
  def short_description(self):
    return self.description[:self.length]

  def __getattr__(self, item):
    return getattr(self.broadcast, item)