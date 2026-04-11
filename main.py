from utils import test

def main():
    filename = "definitions.json"

    test(filename, "physics", "14")
    # test(filename, "physics", ["11", "12"])
    # test(filename, "physics", "all")


if __name__ == "__main__":
    main()
