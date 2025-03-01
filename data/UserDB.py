import pandas as pd
import sqlite3
'''
Databse Management file
'''

df = pd.DataFrame(pd.read_csv("dummy_data.csv"))
print(df)
conn = sqlite3.connect('RallyCats.db')
df.to_sql('Inventory', conn, if_exists='replace', index = False)


# Read in example date
#def setup(cls):

class databse:
    # Read in example date
    def setup(cls):


# Initialize sqlite





# Add item

# Remove item

# Check for expirations

# Check for low quantity
## Ask representative for quantity threshhold