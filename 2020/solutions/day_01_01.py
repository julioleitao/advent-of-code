import sys


def read_entries():
    entries = []

    for line in open(sys.argv[1]):
        entries.append(int(line))

    return entries


def main():
    entries = read_entries()

    for i in range(len(entries)):
        for j in range(len(entries)):
            if i != j and entries[i] + entries[j] == 2020:
                return entries[i] * entries[j]

    return -1


if __name__ == "__main__":
    output = main()
    print(output)
