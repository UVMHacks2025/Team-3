import pandas as pd
import sqlite3
'''
Databse Management file
'''

data = pd.DataFrame(pd.read_csv("dummy_data.csv"))
print(data)




# Read in example data
#def setup(cls):

class databse:
    # Read in example date
    def setup(cls):
        

    



# Add item

    def addItem(cn, n, br, amt, cat, don, veget, kosh, vega, hall):
        cn.execute("""INSERT INTO RALLYCATS (name, brand, quantity, category, 
                   donor, vegetarian, kosher, vegan, hallal) VALUES ({n}, {br},
                   {amt}, {cat}, {don}, {veget}, {kosh}, {vega}, {hall})""")

# Remove item

# Check for expirations

# Check for low quantity
## Ask representative for quantity threshhold