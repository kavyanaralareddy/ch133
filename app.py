# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/index")
def home():

    name = "LOKESHWAR REDDY NARALA" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
# define the route to mother webpage
@app.route("/mother")

# define the route to friends webpage
@app.route("/friend")

# define the route to sister webpage
@app.route("/sister")



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
