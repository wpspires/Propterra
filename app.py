import json
import os
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
Maps_API_Key = '12345'  #os.environ.get("Maps_API_Key")

@app.route("/")
def index():
    return render_template("index.html", Maps_Key=Maps_API_Key)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
