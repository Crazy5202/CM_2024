from flask import Flask, send_file, request
from os import path, mkdir
from shutil import rmtree
from processing.mstiteli_final import process
from threading import Thread

app = Flask(__name__)

storagePath = "./storage"


@app.route("/api/check", methods=["POST"])
def check():
    token = request.form["token"]
    identifier = 1234

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
