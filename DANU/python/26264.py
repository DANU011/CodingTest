def analyze_attention(attention):
    bigData = attention.count('bigdata')
    seCurity = attention.count('security')

    if bigData > seCurity:
        return 'bigdata?'
    elif bigData < seCurity:
        return 'security!'
    else:
        return 'bigdata? security!'

def main():
    N = int(input())
    attention = input()
    result = analyze_attention(attention)
    print(result)

if __name__ == "__main__":
    main()
