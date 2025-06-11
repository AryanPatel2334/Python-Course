#Pandas

import pandas as pd

##a = [1,7,2]
##myvar = pd.Series(a)
##print(myvar)
##
##
##b = [1,7,2]
##myvar1 = pd.Series(a,index=["x","y","z"])
##print(myvar1)


mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset,index=["1.","2.","3."])
print(myvar)
