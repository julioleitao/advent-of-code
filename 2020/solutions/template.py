import sys


def read_entries():
    entries = []

    for line in open(sys.argv[1]):
        entries.append(line.replace("\n", ""))

    return entries


def main():
    return -1


if __name__ == "__main__":
    output = main()
    print(output)
