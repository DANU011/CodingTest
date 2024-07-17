def check_last_character(s):
    last_character = s[-1]
    if last_character in ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']:
        return 1
    else:
        return 0

def main():
    n = input()
    s = input()
    result = check_last_character(s)
    print(result)

if __name__ == "__main__":
    main()
