from flask import Flask, jsonify, url_for

# create an instance of an app
app = Flask(__name__)

students = [
    {"id": 0, "title":"Mr.", "firstname":"Jax", "lastname":"Dev", "course":"DevOps"}
    ]

# use the app.route decorator
# the localhost:5000 is the default port for Flask
# this function runs when the URL is "/"
@app.route("/")
def home():
    return "<h1> Vive la France! </h1>"
# This function runs when the API/URL is accessed

# creating our own API to display data for a specific URL
# this is the URL to navigate to in the browser for this specific view function 
# http://127.0.0.1:5000/api/v1/student/data
@app.route("/api/v1/student/data", methods=["GET"]) 
def greeting():
    return jsonify(students)  
    # Using ETL: Extract Transform Load

# find out the module to redirect the user back to specific page (welcome page
# if page not founds (status code 404, redirect the use to welcome page

# module to redirect user back to specific page
@app.route("/redirectme/")
def redirect_me():
    return redirect(url_for(greeting))


# if any error occurs then redirects to error message page
@app.errorhandler(Exception)
def error_occured(error):
    return redirect(url_for(error_com))

@app.route("/error/")
def error_com():
    return "An error occurred"

# taking arguments
@app.route("/user/<username>/")
def welcome_user(username):
    return f"Welcome {username}"

if __name__ == "__main__":
    app.run(debug=True)
