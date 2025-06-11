#Exercise of pandas

import pandas as pd

purchase = {
    "Name" : ["Laptop","Buds","Smartphone"],
    "Rate" : [52000,1200,18000],
    "Quantity" : [2,5,3],
    "Total" : [104000,3600,54000],
    "Discount" : [4000,200,1500],
    "Net Total" : [100000,3400,52500]
    }

data = pd.DataFrame(purchase,index=["1.","2.","3."])
print(data)

