n, m = map(int, input().split(':'))

def gcd(x, y) :
    while y != 0 :
        x, y = y, x % y
    return x

print(f"{n // gcd(n, m)}:{m // gcd(n, m)}")
