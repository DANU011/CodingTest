def is_palindrome(string):
    string = string.lower()  # Convert to lowercase if needed
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - 1 - i]:
            return "No"
    return "Yes"

if __name__ == "__main__":
    for _ in range(int(input())):
        string = input()
        print(is_palindrome(string))
