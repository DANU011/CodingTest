import sys


def calculate_ranks(R, C, lines):
    history_dict = dict(zip(range(1, 10), [0] * 9))

    for i in range(R):
        line = lines[i].rstrip()

        if line.count('.') == C - 2:
            continue

        kayak_distance = 0

        for char in line[1:-1]:
            if char.isdigit():
                history_dict[int(char)] = kayak_distance
                break

            kayak_distance += 1

    history_list = sorted(history_dict.items(), key=lambda x: -x[1])

    current_rank = 1
    before = -1

    rank_list = [0] * 10

    for kayak, distance in history_list:
        if before < 0:
            before = distance

        if before != distance:
            current_rank += 1

        rank_list[kayak] = current_rank
        before = distance

    return rank_list[1:]


def main():
    input = sys.stdin.read
    data = input().split()
    R = int(data[0])
    C = int(data[1])
    lines = data[2:]

    ranks = calculate_ranks(R, C, lines)

    for rank in ranks:
        print(rank)


if __name__ == "__main__":
    main()
