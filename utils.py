import json, random


def verify_subject(queried_subject, full_data):
    valid_subjects = [subject for subject in full_data]
    if queried_subject not in valid_subjects:
        print("Subject is not in the data")
        return False
    return True

def verify_chapter(queried_subject, queried_chapter, full_data):
    valid_chapters = [chapter for chapter in full_data[queried_subject]]
    if isinstance(queried_chapter, str):
        if not (queried_chapter in valid_chapters or queried_chapter == "all"):
            print("Chapter is either not in the data or not 'all'")
            return False
    elif isinstance(queried_chapter, list):
        for chapter in queried_chapter:
            if chapter not in valid_chapters:
                print(f"'{chapter}' is not a valid chapter")
                print(f"valid_chapters for '{queried_subject}' are {valid_chapters}")
                return False
    else:
        print(
            "datatype for chapter not allowed (including int). use string or list instead"
        )
        return False

    return True


def get_testables_from_chapter(subject_data, chapter):
    testable = []
    for word, definition in subject_data[chapter].items():
        testable.append([word, definition])
    return testable


def get_testables(queried_subject, queried_chapter, full_data):
    testable = []
    subject_data = full_data[queried_subject]
    if queried_chapter == "all":
        for chapter in full_data[queried_subject]:
            testable += get_testables_from_chapter(subject_data, chapter)
    elif isinstance(queried_chapter, list):
        for chapter in queried_chapter:
            testable += get_testables_from_chapter(subject_data, chapter)
    else:  # specified chapter
        testable = get_testables_from_chapter(subject_data, queried_chapter)

    random.shuffle(testable)
    return testable


# def get_random_testable(testable):
    # no_questions = len(testable)
    # random_no = random.randint(0, no_questions - 1)
    # word, definition = testable[random_no]
    # return [word, definition, random_no]


def test(filename, subject, chapter="all"):

    queried_subject = subject
    queried_chapter = chapter

    with open(filename, "r") as f:
        full_data = json.load(f)

    valid = verify_subject(queried_subject, full_data) and verify_chapter(queried_subject, queried_chapter, full_data)
    if not valid:
        return None

    testable = get_testables(queried_subject, queried_chapter, full_data)
    
    total_number_testable = len(testable)

    question_number = 0
    running = True
    print("press 'enter' to reveal or 'q' to quit: \n")
    while running:
        word, definition = testable.pop()
        # testable.pop(index)

        question_number += 1
        print(f"[{question_number}/{total_number_testable}] ", end="")
        print(f"Define: {word}", end="")
        user_input = input()

        if user_input.lower() == "q":
            running = False
            break

        print(f"Answer: {definition}")
        user_input = input()

        if user_input.lower() == "q":
            running = False
        if len(testable) == 0:
            print("All questions tested.")
            running = False

    print("Tester stopped running.")
    return None

# just edit the json with ur friendly neighbourhood text editor

# def add(filename, subject, chapter, word, definition):
#     # expects a json file with a {} in it (i think)
#
#     with open(filename, "r") as f:
#         full_data = json.load(f)
#
#     if not isinstance(chapter, str):
#         print('chapter can only be string')
#         return None
#
#     subject_in_data = verify_subject(subject, full_data)
#
#     if not subject_in_data:
#         print(f"creating new subject '{subject}'")
#         full_data[subject] = {chapter: {word: definition}}
#     else:
#         chapter_in_data = verify_chapter(subject, chapter, full_data)
#         if not chapter_in_data:
#             print(f"creating new chapter '{chapter}' in '{subject}'")
#             full_data[subject][chapter] = {word: definition}
#         else:
#             words_in_chapter = full_data[subject][chapter].keys()
#             if not word in words_in_chapter:
#                 full_data[subject][chapter][word] = definition
#             else:
#                 print(f"'{word}' already exists in data")
#
#     with open(filename, "w") as f:
#         json.dump(full_data, f, indent=2)
#
#     print("operation complete")
#     return None
