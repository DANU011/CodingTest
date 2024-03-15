def bitwise_operations(A, B):
    _and = ''.join(str(int(a) & int(b)) for a, b in zip(A, B))
    _or = ''.join(str(int(a) | int(b)) for a, b in zip(A, B))
    _xor = ''.join(str(int(a) ^ int(b)) for a, b in zip(A, B))
    _notA = ''.join(str(int(not int(a))) for a in A)
    _notB = ''.join(str(int(not int(b))) for b in B)
    
    return _and, _or, _xor, _notA, _notB

def main():
    A = input()
    B = input()
    
    _and, _or, _xor, _notA, _notB = bitwise_operations(A, B)
    
    print(_and)
    print(_or)
    print(_xor)
    print(_notA)
    print(_notB)

if __name__ == "__main__":
    main()
