import sys

def count_unmatched_parentheses(s):
    stack = []
    ret = 0
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                ret += 1
    return ret + len(stack)

def main():
    s = sys.stdin.readline().rstrip()
    result = count_unmatched_parentheses(s)
    print(result)

if __name__ == "__main__":
    main()
