def check_message(m):
    msg, res = [0 for _ in range(26)], 'OK'
    chk = False
    for i in range(len(m)):
        if chk:
            chk = False
            continue
        msg[ord(m[i]) - 65] += 1
        if msg[ord(m[i]) - 65] == 3:
            if i == len(m) - 1:
                res = 'FAKE'
                break
            elif m[i] != m[i + 1]:
                res = 'FAKE'
                break
            chk = True
            msg[ord(m[i]) - 65] = 0
    return res

def main():
    num_cases = int(input())
    for _ in range(num_cases):
        message = input()
        print(check_message(message))

if __name__ == "__main__":
    main()
