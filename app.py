from flask import Flask, render_template, request, flash

app = Flask(__name__) # creates a flask for our app 
app.secret_key = 'sada_sadasAdsd' # creates a secret key for our app

@app.route("/hello") # the /hello represents the last part of our URL
def index():
    flash("What's your name?")
    return render_template('index.html')

@app.route("/greet", methods = ["POST","GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template('index.html')