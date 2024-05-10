from flask import Flask, render_template, request, send_file


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def mainpage():
    return render_template("index.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/team")
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run(port=8080, debug=True, threaded=True)