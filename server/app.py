
#!/usr/bin/env python3

from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    return f"<h3>{parameter}! You actually have to click on the local host to load the webpage</h3>"

@app.route('/count/<int:parameter>')
def count(parameter):
    output = '\n'.join(str(i) for i in range(1, parameter + 1))
    return output

@app.route('/math/<num1><operation><num2>')
def math(num1, operation, num2):
    num1 = unquote(num1)
    num2 = unquote(num2)
    operation = unquote(operation)

    num1 = float(num1)
    num2 = float(num2)
    
    result = None

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == "%":
        result = num1 % num2
    else:
        return "Error: Unsupported operation."

    return f"Result: {result}"
     

if __name__ == '__main__':
    app.run(port=5555, debug=True)