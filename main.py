from flask import Flask, render_template, request, url_for, redirect

import data.UserDB as db

app = Flask(__name__,static_folder='static')


"""
HOME PAGE
"""
@app.route("/", methods = ['GET','POST'])
def home():


    return render_template("home.html")


"""
LOGIN
"""
@app.route("/login", methods = ['GET','POST'])
def login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(password)


        render_template("home.html", user = username)

    return render_template("login.html", user = "")


"""
REGISTER
"""
@app.route("/register", methods = ['GET','POST'])
def register():
    #if login from user


        #user db login info 

    return render_template("register.html")



"""
INVENTORY DASHBOARD
"""
@app.route("/dashboard", methods = ['GET','POST'])
def dashboard():
    # error = 0
    # if request.method == "POST":
    #     quantity = request.form.get("new_quantity") #data verification
    #     if quantity.isdigit():
    #         #Update db with new quantity for inventory
    #         pass
    #     else:
    #         #send message saying the db has not been updated
    #         error = "Invalid Input. Database has not been update."

<<<<<<< HEAD
    # #make rows be all the rows of the db
    # rows = [["Mac and Cheese", "Kraft", 3, "Vegetarian", "3/1/2025", "3/8/2025", "Hannafords"] ]
    
    database = db.Database()
    database.load_db()
    string = database.cur.execute(f'SELECT * FROM Inventory').fetchall()
    print(string)
    return render_template("home.html",
                            string =  string ,
                            )
=======
    #make rows be all the rows of the db
    rows = [["Mac and Cheese", "Kraft", 9, "Vegetarian", "3/1/2025", "3/8/2025", "Hannafords"] ]
    return render_template("inventory.html", 
                           page_title = "Inventory",
                           rows = rows,
                           error = error)
>>>>>>> 4b600647c8a5d5b102fb1b10ecc32f42c150da75

"""
ADD ITEM
"""
@app.route("/add", methods = ['GET','POST'])
def add():
    database = db.Database()
    database.load_db()

    if request.method == "POST":
        name = request.form.get("name")
        amount = request.form.get("amount")
        donor = request.form.get("donor")
        category = request.form.get("category")
        dietary_restrictions = [request.form.get('kosher'), request.form.get('halal'),
                                request.form.get('vegetarian'), request.form.get('vegan')]
        kosher = False 
        halal = False
        vegetarian  = False
        vegan = False
        allergens = [request.form.get('dairy'), request.form.get('eggs'), request.form.get('fish'),
                     request.form.get('shellfish'), request.form.get('tree_nuts'), request.form.get('peanuts'),
                     request.form.get('wheat'), request.form.get('soybeans'), request.form.get('sesame')]
        
        tag_list = request.form.get('tags')
        tags = tag_list.split(',')
        for i in range(0, len(tags)):
            tags[i] = tags[i].strip()

        for i in range(len(dietary_restrictions)):
            if dietary_restrictions[i] == 'kosher':
                kosher = True
            elif dietary_restrictions[i] == 'vegetarian':
                vegetarian = True
            elif dietary_restrictions[i] == 'halal':
                halal = True
            elif dietary_restrictions[i] == 'vegan':
                vegan = True

        date = request.form.get('date')
        requested = request.form.get('requested')
        

        database.addItem(name,None,amount,category,donor,vegetarian,kosher,vegan,halal)
        # TODO: Put into database


    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)