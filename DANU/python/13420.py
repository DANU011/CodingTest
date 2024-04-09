def calculate(input_str):
    li = input_str.split()
    a, b, c = int(li[0]), int(li[2]), int(li[4])
    op = li[1]
    if op == '+':
        t = a + b
    elif op == '-':
        t = a - b
    elif op == '*':
        t = a * b
    elif op == '/':
        t = a // b
    return "correct" if t == c else "wrong answer"

def main():
    num_tests = int(input())
    for _ in range(num_tests):
        input_str = input()
        result = calculate(input_str)
        print(result)

if __name__ == "__main__":
    main()
