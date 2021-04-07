from flask import Flask, render_template, request


MY_EMAIL = "akshitgaur.sky21@gmail.com"
MY_PASSWORD = "8xZ*XHKJ%7eJbB"
SEND_MAIL = "akshit.gaur1214@gmail.com"

from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template("index.html")


@app.route('/content-left', methods=['GET', 'POST'])
def left_bar():
    if request.method == 'GET':
        return render_template("left-sidebar.html")


@app.route('/content-no', methods=['GET', 'POST'])
def no_bar():
    if request.method == 'GET':
        return render_template("no-sidebar.html")


@app.route('/content-right', methods=['GET', 'POST'])
def right_bar():
    if request.method == 'GET':
        return render_template("right-sidebar.html")


if __name__ == "__main__":
    app.run(debug=True)
