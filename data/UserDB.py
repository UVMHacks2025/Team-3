import pandas as pd
import sqlite3
'''
Databse Management file
'''

class Database:
    # Read in example date
    def __init__(self):
        self.cn = sqlite3.connect('RallyCats.db')
        self.inventory_df = pd.DataFrame(pd.read_csv("dummy_data.csv"))
        self.users_df = pd.DataFrame(pd.read_csv("user_data.csv"))

    def load_db(self):
        cn = sqlite3.connect('RallyCats.db')
        self.inventory_df.to_sql('Inventory', cn, if_exists='replace', index=False)
        self.users_df.to_sql('Users', cn, if_exists='replace', index=False)
        print(self.inventory_df)



    # Add item
    def addItem(self, n, br, amt, cat, don, veget, kosh, vega, hall):
        self.cn.execute("""INSERT INTO RALLYCATS (name, brand, quantity, category, 
                   donor, vegetarian, kosher, vegan, hallal) VALUES ({n}, {br},
                   {amt}, {cat}, {don}, {veget}, {kosh}, {vega}, {hall})""")
        self.cn.commit()

# Remove item
    def removeItem(self, n):
        self.cn.execute("""DELETE FROM RALLYCATS WHERE name = {n}""")
        self.cn.commit()

# Change quantity
    def changeQuantity(self, n, amt):
        self.cn.execute("""UPDATE RALLYCATS SET quantity = {amt} WHERE name = {n}""")
        self.cn.commit()
    # Change quantity
    def changeQuantity(self, n, amt):
        self.cn.execute("""UPDATE RALLYCATS SET quantity = {amt} WHERE name = {n}""")
        self.cn.commit()

    # Check for expirations

    # Check for low quantity
    ### Ask representative for quantity threshhold



def Testing():
    db = Database()
    db.load_db()

    print("\n--- Running Tests ---")

    # Add a test item
    db.addItem("Test Item", "Test Brand", 10, "non-perishable", 1, 1, 1, 1, 1)

    # Change quantity of test item
    db.changeQuantity("Test Item", 25)

    # Remove test item
    db.removeItem("Test Item")

    print("\n--- Tests Completed Successfully ---")


if __name__ == '__main__':
    Testing()
