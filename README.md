##  MVC with Flask

### MVC = "Model View Controller"

1. Display data on a web browser using HTML, CSS, JavaScript and Bootstrap

2. Building our API

3. Display data from Flask to a specific API call/URL/endpoint

### Why Flask for our framework?
```
- Flask is a mini web app frame work but very powerful
- Allows us to interact with a DB
- It can be used to create an API
- Allows us to integrate with HTMl, CSS and JS
- Allows us to map HTTP requests to Python e.g. URL and HTTP GET
- Allows us to set the API path as URL to view in the browser
```
### Tutorial

- Ensure it is installed with pip install flask
- Import with
```
from flask import Flask, jsonify, redirect, url_for
```
- Run the flask app with flask run
- Initialise the flask with
```
app = Flask(__name__)
```
#### Flask Features

- JSONIFY
Return JSON with jsonify
```
students = [
    {"id": 0, "title": "Mr.", "first_name": "Leo", "last_name": "Waltmann", "course": "DevOps"}
]
@app.route("/api/v1/student/data", methods = ["GET"])
def customised_api():
    # Extact Transform Load
    # Transforms data into JSON
    return jsonify(students)
```
- REDIRECT and URL_FOR
```
- Redirects to different url
- Use url_for to refer to the function instead of typing out the whole URL
```
```
@app.route("/redirectme/")
def redirect_me():
    return redirect(url_for(greet_user))
```

#### ERROR REDIRECTING

- Use app.errorhandler(Exception) to redirect to a given page in case of any errors
```
# if any error occurs then redirects to error message page
@app.errorhandler(Exception)
def error_occured(error):
    return redirect(url_for(error_message))

@app.route("/error/")
def error_message():
    return "An error occurred, sorry"
```
#### PASSING ARGUMENTS

- Can pass arguments with <> in url which then passes argument to function
```
# taking arguments
@app.route("/user/<username>/")
def welcome_user(username):
    return f"Welcome {username}"
```
