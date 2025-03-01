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

        #user db login info 

    return render_template("register.html",username,password)



"""
INVENTORY DASHBOARD
"""
@app.route("/dashboard", methods = ['GET','POST'])
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug=True)


