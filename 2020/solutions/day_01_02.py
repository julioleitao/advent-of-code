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
            for k in range(len(entries)):
                if len({i, j, k}) == 3 and entries[i] + entries[j] + entries[k] == 2020:
                    return entries[i] * entries[j] * entries[k]

    return -1


if __name__ == "__main__":
    output = main()
    print(output)
