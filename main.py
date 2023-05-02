from flask import Flask, jsonify
import datetime
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
        result = {
            "number": num,
            "Armstrong": True,
            "Server": f"/armstrong/{num}",
            "message": "The input number is not an Armstrong number",
            "timestamp": str(datetime.datetime.now())

        }
    else:
        result = {
            "number": num,
            "Armstrong": False,
            "Server": f"/armstrong/{num}",
            "message": "The input number is not an Armstrong number",
            "timestamp": str(datetime.datetime.now())
        }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
