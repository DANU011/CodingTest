def process_input(s, input_string):
    count_e = input_string.count('e')
    result = ['2', 'e', 'yee'][(count_e > s - count_e) + ((s - count_e) == count_e) * 2]
    return result

def main():
    import sys
    input = sys.stdin.readline

    s = int(input().rstrip())
    input_string = input().rstrip()
    print(process_input(s, input_string))

if __name__ == "__main__":
    main()
