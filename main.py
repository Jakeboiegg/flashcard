from utils import Flashcard
from flask import Flask, render_template, request

filename = "static/definitions.json"
flashcard = Flashcard(filename)

# init flask app
app = Flask(__name__)

subject = "physics" # hard coded 'physics' for now

@app.route("/", methods=["GET", "POST"])
def index():
    testables = [["nothing is selected", "go select a chapter and submit it"]]
    if request.method == "POST":
        subjects = [subject for subject in request.form]
        testables = flashcard.get_testables(subject, subjects)

    chapters = flashcard.get_chapters(subject)
    return render_template("index.html", chapters=chapters, testables=testables)

if __name__ == "__main__":
    app.run(debug=True)
