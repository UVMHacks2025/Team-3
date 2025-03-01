import pandas as pd
import sqlite3
'''
Databse Management file
'''

class databse:
    # Read in example date
    def __init__(self, df):
        self.df = df
        df = pd.DataFrame(pd.read_csv("dummy_data.csv"))
        cn = sqlite3.connect('RallyCats.db')
        df.to_sql('Inventory', cn, if_exists='replace', index=False)
# Initialize sqlite





# Add item

    def addItem(cn, n, br, amt, cat, don, veget, kosh, vega, hall):
        cn.execute("""INSERT INTO RALLYCATS (name, brand, quantity, category, 
                   donor, vegetarian, kosher, vegan, hallal) VALUES ({n}, {br},
                   {amt}, {cat}, {don}, {veget}, {kosh}, {vega}, {hall})""")

# Remove item

# Check for expirations

# Check for low quantity
## Ask representative for quantity threshhold