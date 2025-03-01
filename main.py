from flask import Flask, render_template, request, url_for, redirect

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
    #if login from user
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')


    return render_template("home.html")



"""
INVENTORY DASHBOARD
"""
@app.route("/dashboard", methods = ['GET','POST'])
def dashboard():
    if request.method == "POST":
        quantity = request.form.get("new_quantity") #data verification
        if quantity.isDigit():
            #Update Database with new quantity for inventory
            pass
        else:
            #send message saying the db has not been updated
            error = "Invalid Input. Database has not been update."

    rows = [["Mac and Cheese", "Kraft", "3", "Vegetarian", "3/1/2025", "3/8/2025", "Hannafords"] ]#update with database
    return render_template("inventory.html", 
                           page_title = "Inventory",
                           rows = rows,
                           error = error)

"""
ADD ITEM
"""
@app.route("/add", methods = ['GET','POST'])
def add():
    return render_template("add.html")

