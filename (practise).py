# coding: utf-8
import numpy as np
import pandas as pd
a = [[1,2,3,4], [3,4,5,6], [2,7,8,5], [6,5,4,3],[4,2,3,2]]
a
np.array(a)
a = np.array(a)
a
b = np.random.randint((5,4))
b
pd.DataFrame(a)
pd.DataFrame(a, colum=('first', 'second', 'third', 'fourth'))
pd.DataFrame(a, column=('first', 'second', 'third', 'fourth'))
pd.DataFrame(a, column = 'first', 'second', 'third', 'fourth')
get_ipython().run_line_magic('save', '("numpy practise")')
get_ipython().run_line_magic('save', '(numpy practise)')
get_ipython().run_line_magic('save', '()')
