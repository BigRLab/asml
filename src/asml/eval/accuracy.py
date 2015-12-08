from eval import Eval
import numpy as np

class Accuracy(Eval):
  def __init__(self):
    Eval.__init__(self)
    self._correct = 0
    self._instances = 0

  def stream_evaluate(self, truth, pred):
    self._correct += np.sum(truth == pred)
    self._instances += truth.shape[0]
    return float(self._correct) / self._instances

  def evaluate(self, truth, pred):
    return float(np.sum(truth == pred)) / truth.shape[0]

  def __str__(self):
    return 'accuracy'