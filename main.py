import utils

def main():
    filename = "static/definitions.json"

    testables = utils.get_testables(filename, "physics", "14")
    print(testables)

    # utils.test(filename, "physics", "14")

if __name__ == "__main__":
    main()
