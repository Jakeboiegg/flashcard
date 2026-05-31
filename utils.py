import json

class Flashcard:
    def __init__(self, filename):
        with open(filename, "r") as f:
            self.full_data = json.load(f)

    def get_testables_from_chapter(self, subject_data, chapter):
        # internal function used in get_tastables()

        testable = []
        for word, definition in subject_data[chapter].items():
            testable.append([word, definition])
        return testable


    def get_testables(self, queried_subject, queried_chapter):
        # queried_chapter can be a list of chapters
        testable = []
        subject_data = self.full_data[queried_subject]

        if queried_chapter == "all":
            for chapter in self.full_data[queried_subject]:
                testable += self.get_testables_from_chapter(subject_data, chapter)
        elif isinstance(queried_chapter, list):
            for chapter in queried_chapter:
                testable += self.get_testables_from_chapter(subject_data, chapter)
        else:  # specified chapter
            testable = self.get_testables_from_chapter(subject_data, queried_chapter)

        return testable
