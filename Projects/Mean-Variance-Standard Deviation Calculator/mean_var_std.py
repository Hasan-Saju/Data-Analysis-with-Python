import numpy as np

def calculate(List):

  calculations={}
  num = len(List)
  if num<9:
    raise ValueError("List must contain nine numbers.")

  npa=np.array([List[0:3],
              List[3:6],
              List[6:9]
              ])

  meann=[list(npa.mean(axis=0)),list(npa.mean(axis=1)),npa.mean()]
  variance=[list(npa.var(axis=0)),list(npa.var(axis=1)),npa.var()]
  stdv=[list(npa.std(axis=0)),list(npa.std(axis=1)),npa.std()]
  mx=[list(npa.max(axis=0)),list(npa.max(axis=1)),npa.max()]
  mn=[list(npa.min(axis=0)),list(npa.min(axis=1)),npa.min()]
  sm=[list(npa.sum(axis=0)),list(npa.sum(axis=1)),npa.sum()]

  calculations={
    'mean':meann,
    'variance':variance,
    'standard deviation':stdv,
    'max':mx,
    'min':mn,
    'sum':sm
  }
  return calculations