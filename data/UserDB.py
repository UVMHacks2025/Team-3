import pandas as pd
import sqlite3
'''
Databse Management file
'''

data = pd.DataFrame(pd.read_csv("dummy_data.csv"))
print(data)




# Read in example date
#def setup(cls):

class databse:
    # Read in example date
    def setup(cls):
        database = sqlite3.connect()
        cls = database.cursor()


# Initialize sqlite

    



# Add item



# Remove item

# Check for expirations

# Check for low quantity
## Ask representative for quantity threshhold