import sys

sys.path.insert(0, r'c:\classroom\sep21\demo\mylib')
print(sys.path)

import num_funs as nf
from num_funs import iseven

print(nf.iseven(10))
print(iseven(10))
