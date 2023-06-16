import numpy as np
from CnfResolver import CnfResolver

cn = CnfResolver("input.cnf")

a = np.array([[1, 3, 4, 5],
              [2, 4, 5, 6],
              [1, 2, 3, 4],
              [10, 20, 30, 40]])
print(a[0:3][0:2])
