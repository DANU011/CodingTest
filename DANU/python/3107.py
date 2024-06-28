def expand_ipv6(ipv6):
    ipv6 = ipv6.split(':')
    if ipv6[0] == '':
        ipv6 = ipv6[1:]
    if ipv6[-1] == '':
        ipv6 = ipv6[:-1]

    result = ''
    for i in ipv6:
        if i == '':
            result += '0000:' * (8 - len(ipv6) + 1)
        else:
            result += i.zfill(4) + ':'

    return result[:-1]

def main():
    ipv6 = input()
    expanded_ipv6 = expand_ipv6(ipv6)
    print(expanded_ipv6)

if __name__ == "__main__":
    main()
