from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    dictionary = {"nickname": "Kakkun", "age": 20, "address": "北海道"}
    list = []
    command = False
    for i in range(10):
        list.append(i)

    return render_template('flaskQ.html', list=list, dictionary=dictionary, command=command)


if __name__ == "__main__":
    app.run(port=8000)
