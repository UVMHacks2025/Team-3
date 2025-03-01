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
def home():
    #if login from user
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')


    return render_template("home.html")



"""
INVENTORY DASHBOARD
"""
@app.route("/dashboard", methods = ['GET','POST'])
def home():
    return render_template("home.html")



