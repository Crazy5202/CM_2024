from flask import Flask, render_template, request, send_file
from os import path, mkdir

if not path.isdir("./storage"):
    mkdir("./storage")


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def mainpage():
    if request.method == "GET":
        return render_template("index.html")
    else:
        data = request.files["fileToUpload"].read()
        target = open("./storage/recieved.pdf", mode='wb')
        if target.closed:
            print("file was not opened")
            return render_template("index.html")
        target.write(data)
        # processing target
        # ...
        return send_file("./storage/recieved.pdf")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/team")
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run(port=8080, debug=True)