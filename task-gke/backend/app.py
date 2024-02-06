import random, string
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/")
def index():
    return "HELLO"

@app.route("/generate")
def index_generate():
    random_string = ''.join(random.choice(string.ascii_letters) for i in range(10))
    return "v1-" + random_string

if __name__=="__main__":
    app.run(host='0.0.0.0', port=80, debug=True)