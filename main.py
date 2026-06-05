from utils import Flashcard
from flask import Flask, render_template

filename = "static/definitions.json"
flashcard = Flashcard(filename)

testables = flashcard.get_testables("physics", "14")

# init flask app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
