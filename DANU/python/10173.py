def find_nemo():
    while True:
        moon = input()
        if moon == "EOI":
            break
        print("Found" if "nemo" in moon.lower() else "Missing")

if __name__ == "__main__":
    find_nemo()
