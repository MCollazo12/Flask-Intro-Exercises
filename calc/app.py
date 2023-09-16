"""
A simple calculator using Flask
"""

from flask import Flask,request
from operations import *

app = Flask(__name__)

@app.route("/add")
def add_page():
    """Add a and b parameters and return result."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def sub_page():
    """Subtract and b parameters and return result."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def mul_paget():
    """Multiply a and b parameters and return result."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.route("/div")
def div_page():
    """Divide a and b parameters and return result."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

@app.route('/math/<operation>')
def handle_math(operation):
    
    math = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div,
    }
    
    a = request.args.get('a')
    b = request.args.get('b')
    
    if operation in math and a and b:
        result = math[operation](float(a), float(b))
    else:
        return 'You must include values for a and b'
    
    return f"""
    <body>
        <h2>{round(result, 2)}</h2>
    </body>
    """
