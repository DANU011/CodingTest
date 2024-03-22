def process_input(a):
    if a == "***":
        return False
    else:
        print(a[::-1])
        return True

def main():
    while True:
        a = input()
        if not process_input(a):
            break

if __name__ == "__main__":
    main()
