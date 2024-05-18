from flask import Flask, send_file, request
from os import path, mkdir, environ
from shutil import rmtree
from processing.mstiteli_final import process
from flask_request_id import RequestID

app = Flask(__name__)
RequestID(app)

storagePath = "./storage"


@app.route("/api/check", methods=["POST"])
def check():
    token = request.form["token"]
    if token != environ["TOKEN"]:
        return "401 error", 401
    identifier = request.environ.get("REQUEST_ID")

    data = request.files["file"].read()
    app.logger.debug("File has been recieved")
    if not path.exists(f"{storagePath}"):
        mkdir(f"{storagePath}")
    if not path.exists(f"{storagePath}/{identifier}"):
        mkdir(f"{storagePath}/{identifier}")
    targetFile = open(f"{storagePath}/{identifier}/target.pdf", mode='wb')
    targetFile.write(data)

    process(f"{storagePath}/{identifier}")
    app.logger.debug("Success!")

    response = send_file(f"{storagePath}/{identifier}/output.pdf")
    rmtree(f"{storagePath}/{identifier}")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    context = ("./cert/cert.crt", "./cert/privkey.key")
    app.run(host='0.0.0.0', port=3000, debug=True,
            threaded=True, ssl_context=context)
