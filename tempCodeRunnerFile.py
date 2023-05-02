from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/armstrong/<int:num>')
def is_armstrong_number(num):
    order = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        return "True"
    else:
        return "False"


if __name__ == "__main__":
    app.run(debug=True)
