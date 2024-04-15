def calculate(input_str):
    li = ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']
    for c in input_str:
        li.remove(c)
    return ''.join(li)

def main():
    s = input()
    result = calculate(s)
    print(result)

if __name__ == "__main__":
    main()
