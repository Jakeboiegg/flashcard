from utils import Flashcard
from flask import Flask, render_template, request

filename = "static/definitions.json"
flashcard = Flashcard(filename)

# init flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        for item in request.form:
            print(item)

    chapters = flashcard.get_chapters("physics") # hard coded 'physics for now'
    return render_template("index.html", chapters=chapters)

if __name__ == "__main__":
    app.run(debug=True)
