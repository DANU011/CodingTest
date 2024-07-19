def create_palindrome(N, palindrome):
    for i in range(N):
        if palindrome[i].isalpha():
            palindrome[-i - 1] = palindrome[i]

    for i in range(N):
        if palindrome[i] == "?":
            palindrome[i] = "a"

    return "".join(palindrome)

def main():
    N = int(input())
    palindrome = list(input())
    result = create_palindrome(N, palindrome)
    print(result)

if __name__ == "__main__":
    main()
