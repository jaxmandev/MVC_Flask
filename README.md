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

# STEP BY STEP

- Now we will look at the app from above, line by line.
- Import Flask and create an application object
- We begin here, with two lines you will see in every Flask app:
```
from flask import Flask
app = Flask(__name__)
```
#### The first line
```
is a typical Python import statement. Lowercase flask is a Python library, which you have installed. Uppercase Flask is a class from that library, and it must be imported. As always, case matters, so note the lowercase f and the uppercase F.
```
#### The second line
```
 which is new to you, begins with a new variable, app, which will be used in every Flask app. The value of that new variable, Flask(__name__), is a new object that inherits from the class Flask — meaning it gets all the attributes and methods built into that class, which we have imported.
```
__name__ is a built-in variable in Python. Python has many double-underscore entities, and they always have this pattern: two underscores, a word, and two underscores. These double-underscore entities are referred to with the slang dunder. For __name__, we can say “dunder name.”

What does __name__ do? Every Python module has a name, and __name__ used in a module contains the name of that module. The value of __name__ is not always the filename, as demonstrated in a common Python statement:

if __name__ == '__main__':
When that statement returns True, it means the program (the file) is being run by itself, and was not imported. (We are NOT using that statement in our hello.py code, but this seems like a good time to explain it.)

app = Flask(__name__) creates a Flask application object — app — in the current Python module. A Python module is just a Python file, filename.py. An object (in Python and in other programming languages) is a data type that can include a ton of functions, methods, and attributes. Our variable app now has all of those from Flask. To be specific, app is an instance of a Python class named Flask, which we imported at the top of the file.

Basically, we have brought into this file — this app — all the capabilities of Flask.

Add a route and some action

This next part of your first Flask app is what does the work.

@app.route('/')
def hello():
    return 'Hello World!'
It consists of two parts: the decorator and the function that is “decorated.”

A decorator begins with @ and is a unique feature of the Python language. It modifies the function that follows it. Let that sink in.

The decorator:

@app.route('/')
Remember that app is a Flask application object. It has all the methods and attributes of the Flask class, and one of those is route(), which expects to be used in exactly this way — in a decorator.
The contents of the parentheses are a path — a partial URL.
Your Flask application will perform different actions depending on which URL is sent to it. '/' is the root of the website, the top, the home page. @app.route('/index') indicates a URL such as localhost:5000/index or (on a live server) https://mydomain.com/index. Note that there is no file there — no .html.
The action that will be performed at that URL depends on what is written in the function that immediately follows the decorator.
The function:

def hello():
    return 'Hello World!'
All this function does is return a simple string: 'Hello World!' Our Flask app performs this action when the server is running, the app is running, and we open localhost:5000 in the browser. (Naturally, a Flask app can run on a live web server.)

Note that there does not need to be any relationship between the decorator and the function except proximity:

@app.route('/')
def hello():
    return 'Hello World!'
Often people writing a Flask app use the same word for the route and the function, like so:

@app.route('/foobar')
def foobar():
    return 'Hi there, foobar!'
There’s nothing wrong with this, but it’s not necessary. Use it if you like it.

Modify hello.py: Add a new route

Add these three lines to your hello.py file and save it.

@app.route('/foobar')
def foobar():
    return '<h1>Hi there, foobar!</h1>'
Repeat the steps from above to run the file and open localhost:5000.

After you see Hello World! in the browser (the same as before), type localhost:5000/foobar into the address bar and press Enter or Return. That is what the new, added route made possible.

Example of a new Flask route screenshot
It is possible to have many different routes in one Flask app, and each route can do an entirely different thing.


if __name__ == '__main__':
    app.run(debug=True)

Because of the final two lines in this script, you will run thi
file in exactly the same way you’ve run every other .py file in 
virtual environment:
```
python hello3.py
```
Do not use flask run to run this script. That is not necessary, thanks to lines 20 and 21.