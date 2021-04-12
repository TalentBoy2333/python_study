import sys 
import os
sys.path.append(os.path.abspath('..'))

from A.myfun import myadd

print(sys.path)
print(myadd(1,2,3))