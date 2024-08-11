import os

from flask import Flask, send_file
from sqlalchemy import MetaData
from eralchemy2 import render_er

from connection import engine

app = Flask(__name__)


@app.route("/generate")
def make_erd():

    if not all(
        [
            os.getenv("DB_USERNAME"),
            os.getenv("DB_PASSWORD"),
            os.getenv("DB_SERVER"),
            os.getenv("DB_DATABASE"),
        ]
    ):
        return "Missing database credentials", 400

    # get metadata object
    metadata = MetaData()
    metadata.reflect(bind=engine)

    # create the pydot graph object by autoloading all tables via a bound metadata object
    render_er(metadata, "erd.png")

    return send_file("erd.png", mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
