def palindrome_check(s, left, right, count) :
    if left >= right :
        return [1, count]
    elif s[left] != s[right] :
        return [0, count]
    else :
        return palindrome_check(s, left + 1, right - 1, count + 1)

def is_palindrome(s, count) :
    return palindrome_check(s, 0, len(s) - 1, count)

for _ in range(int(input())) :
    input_string = input()
    print(*is_palindrome(input_string, 1))
