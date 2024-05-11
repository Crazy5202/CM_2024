from flask import Flask, render_template


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
    context = ("./cert/cert.crt", "./cert/privkey.key")
    app.run(port=443, debug=True, threaded=True, ssl_context=context)
