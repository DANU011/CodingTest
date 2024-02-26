from hashlib import sha256

def hash_data(data):
    return sha256(data.encode()).hexdigest()

def main():
    data = input()
    hashed_data = hash_data(data)
    print(hashed_data)

if __name__ == "__main__":
    main()
