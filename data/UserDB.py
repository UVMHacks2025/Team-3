import pandas as pd
import sqlite3
'''
Database Management file
'''

class Database:
    # Read in example date
    def __init__(self):
        self.cn = sqlite3.connect('RallyCats.db')
        self.cur = self.cn.cursor()
        self.inventory_df = pd.DataFrame(pd.read_csv("dummy_data.csv"))
        self.users_df = pd.DataFrame(pd.read_csv("user_data.csv"))

    def load_db(self):
        cn = sqlite3.connect('RallyCats.db')
        self.inventory_df.to_sql('Inventory', cn, if_exists='replace', index=False)
        self.users_df.to_sql('Users', cn, if_exists='replace', index=False)
        #print(self.inventory_df)



    # Add item

    def addItem(self, n, br, amt, cat, don, veget, kosh, vega, hall):
        query = """INSERT INTO Inventory (name, brand, quantity, category, 
                       donor, vegetarian, kosher, vegan, hallal) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        self.cur.execute(query, (n, br, amt, cat, don, veget, kosh, vega, hall))
        self.cn.commit()

# Remove item
    def removeItem(self, n):
        query = ("""DELETE FROM Inventory WHERE name = ?""")
        self.cur.execute(query, (n,))
        self.cn.commit()

    # Change quantity
    def changeQuantity(self, n, amt):
        query = """UPDATE Inventory SET quantity = ? WHERE name = ?"""
        self.cur.execute(query, (amt, n))
        self.cn.commit()
        self.cn.commit()

    # Check for expirations

    # Check for low quantity
    #returns a list of [name, quantity]
    def lowQuanity(self):
        self.cur.execute("""SELECT * FROM Inventory WHERE quantity <= 5""")
        low = self.cur.fetchall()
        output = []
        for i in low:
            output.append([i[0], i[2]])
        return output

    ### Ask representative for quantity threshhold - its 5



def Testing():
    db = Database()
    db.load_db()

    # Add a test item
    db.addItem("Test Item", "Test Brand", 10, "non-perishable", 1, 1, 1, 1, 1)

    # Change quantity of test item
    db.changeQuantity("Test Item", 25)

    print(db.lowQuanity())

    # Remove test item
    #db.removeItem("Test Item")

    print("\n--- Tests Completed Successfully ---")


if __name__ == '__main__':
    Testing()
