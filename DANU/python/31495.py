def process_code(code):
    if code[0] == code[-1] == '"' and len(code[1:-1]) > 0:
        return code[1:-1]
    else:
        return "CE"

def main():
    code = input()
    result = process_code(code)
    print(result)

if __name__ == "__main__":
    main()
