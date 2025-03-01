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
    #if login from user

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
    error = 0
    #make rows be all the rows of the db
    database = db.Database()
    database.load_db()
    rows = database.cur.execute("SELECT * FROM Inventory").fetchall()
    if request.method == "POST":
        if request.form.get('button') == "Delete":
            item_name = request.form.get("button")
            db.removeItem(item_name)
        elif request.form.get('button') == "Update":
            quantity = request.form.get("new_quantity") #data verification
            item_name = request.form.get("button")
            #TESTING
            print(item_name)
            if quantity.isdigit():
                #Update db with new quantity for inventory
                db.changeQuantity(item_name, quantity)
            else:
                #send message saying the db has not been updated
                error = "Invalid Input. Database has not been update."

    
    #rows = [["Mac and Cheese", "Kraft", 9, "Vegetarian", "3/1/2025", "3/8/2025", "Hannafords"] ]
    return render_template("inventory.html", 
                           page_title = "Inventory",
                           rows = rows,
                           error = error)

"""
ADD ITEM
"""
@app.route("/add", methods = ['GET','POST'])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        donor = request.form.get("donor")
        dietary_restrictions = [request.form.get('kosher'), request.form.get('halal'),
                                request.form.get('vegetarian'), request.form.get('vegan')]
        allergens = [request.form.get('dairy'), request.form.get('eggs'), request.form.get('fish'),
                     request.form.get('shellfish'), request.form.get('tree_nuts'), request.form.get('peanuts'),
                     request.form.get('wheat'), request.form.get('soybeans'), request.form.get('sesame')]
        tag_list = request.form.get('tags')
        tags = tag_list.split(',')
        for i in range(0, len(tags)):
            tags[i] = tags[i].strip()

        date = request.form.get('date')
        requested = request.form.get('requested')

        # TODO: Put into database


    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)