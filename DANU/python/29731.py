def check_promise(N):
    promise = [
        "Never gonna give you up",
        "Never gonna let you down",
        "Never gonna run around and desert you",
        "Never gonna make you cry",
        "Never gonna say goodbye",
        "Never gonna tell a lie and hurt you",
        "Never gonna stop",
    ]

    for _ in range(N):
        p = input()
        if p not in promise:
            return "Yes"
    return "No"

def main():
    N = int(input())
    result = check_promise(N)
    print(result)

if __name__ == "__main__":
    main()
