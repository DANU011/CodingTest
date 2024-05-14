def encrypt_message(a, b, s):
    encrypted = ''.join([chr(ord('A') + ((ord(c) - ord('A')) * a + b) % 26) for c in s])
    return encrypted

def main():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        s = input()
        result = encrypt_message(a, b, s)
        print(result)

if __name__ == "__main__":
    main()
