def count_hello_bit(friends, HelloBit):
    return friends.count(HelloBit)

def main():
    N = int(input())
    friends = input().split()
    HelloBit = input()
    result = count_hello_bit(friends, HelloBit)
    print(result)

if __name__ == "__main__":
    main()
