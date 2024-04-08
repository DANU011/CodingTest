def check_string_repeat(s, t):
    slen, tlen = len(s), len(t)
    return 1 if slen * t == tlen * s else 0

if __name__ == "__main__":
    s = input()
    t = input()
    print(check_string_repeat(s, t))
