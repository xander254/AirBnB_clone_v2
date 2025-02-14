#!/usr/bin/python3
from flask import Flask

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/", strict_slashes=False)
    def hello_hbnb():
        return "<p>Hello HBNB!</p>"
    app.run(host="0.0.0.0", port=5000, debug=True)  
    print("Starting Flask app...")
