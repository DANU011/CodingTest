def balance_binary_string(s):
    n = list(s)
    zero = n.count('0') // 2
    one = n.count('1') // 2
    
    for _ in range(zero):
        n.pop(-(n[::-1].index('0') + 1))
    
    for _ in range(one):
        n.pop(n.index('1'))
    
    return ''.join(n)

def main():
    s = input()
    result = balance_binary_string(s)
    print(result)

if __name__ == "__main__":
    main()
