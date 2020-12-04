import sys


def read_entries():
    entries = []

    for line in open(sys.argv[1]):
        entries.append(line.replace("\n", ""))

    return entries


def is_valid(policy, letter, password):
    lowest, highest = policy.split("-")
    lowest, highest = int(lowest), int(highest)

    letter = letter[0]

    count = 0

    for c in password:
        if c == letter:
            count += 1

    return count <= highest and count >= lowest


def main():
    count = 0

    for line in read_entries():
        policy, letter, password = line.split(" ")
        if is_valid(policy, letter, password):
            count += 1

    return count


if __name__ == "__main__":
    output = main()
    print(output)
