##### KMP 알고리즘 getPi() ######
import sys
input_reader = sys.stdin.readline

def get_min_possible_length(string):
    length = len(string)
    prefix_lengths = [0] * length
    j = 0

    for i in range(1, length):
        while j > 0 and string[i] != string[j]:
            j = prefix_lengths[j - 1]

        if string[i] == string[j]:
            j += 1
            prefix_lengths[i] = j

    return length - prefix_lengths[-1]

if __name__ == '__main__':
    total_length = int(input_reader())
    screen_content = str(input_reader().rstrip())

    min_possible_length = get_min_possible_length(screen_content)
    print(min_possible_length)
