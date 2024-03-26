def toggle_string(s):
    return ''.join('1' if char == '0' else '0' for char in s)

def check_deletion_success(N, a, b):
    for _ in range(N):
        a = toggle_string(a)
    return "Deletion succeeded" if a == b else "Deletion failed"

def main():
    N = int(input())
    a = input()
    b = input()
    result = check_deletion_success(N, a, b)
    print(result)

if __name__ == "__main__":
    main()
