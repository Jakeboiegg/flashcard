from utils import Flashcard
from flask import Flask, render_template, request

filename = "static/definitions.json"
flashcard = Flashcard(filename)

testables = flashcard.get_testables("physics", "14")

# init flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        for item in request.form:
            print(item)

    chapters = [
            "topic 1",
            "topic 2",
            "topic 3",
            "topic 4",
            "topic 5",
            ]
    return render_template("index.html", chapters=chapters)

if __name__ == "__main__":
    app.run(debug=True)
