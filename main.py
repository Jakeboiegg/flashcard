from utils import Flashcard
from flask import Flask, render_template, request

filename = "static/definitions.json"
flashcard = Flashcard(filename)

# init flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    testables = [["nothing is selected", "go select a chapter and submit it"]]
    subject = "physics" # default subject
    if request.method == "POST":
        subject = request.form["subject"]
        chapters_to_test = [chapter for chapter in request.form if chapter != "subject"]
        testables = flashcard.get_testables(subject, chapters_to_test)

    chapters = flashcard.get_chapters(subject)

    # find subject and shuffle current subject to the front of the list
    all_subjects = flashcard.get_all_subjects()
    for i in range(len(all_subjects)):
        if all_subjects[i] == subject:
            all_subjects.pop(i)
            all_subjects = [subject] + all_subjects
            break

    return render_template("index.html", all_subjects=all_subjects, chapters=chapters, testables=testables)

if __name__ == "__main__":
    app.run(debug=True)
