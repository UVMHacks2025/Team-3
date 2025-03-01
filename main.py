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
    if request.method == 'POST':
        #posted to the server 
        username = request.form.get('username')
        print(username)
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
    if request.method == "POST":
        quantity = request.form.get("new_quantity") #data verification
        if quantity.isDigit():
            #Update Database with new quantity for inventory
            pass
        else:
            #send message saying the db has not been updated
            error = "Invalid Input. Database has not been update."

    rows = ["Mac and Cheese", "Kraft", "3", "Vegetarian", "3/1/2025", "3/8/2025", "Hannafords"] #update with database
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

if __name__ == "__main__":
    app.run(debug=True)