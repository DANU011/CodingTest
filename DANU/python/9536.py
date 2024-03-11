import sys

def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        sound = list(map(str, sys.stdin.readline().split()))

        while True:
            animal = list(map(str, sys.stdin.readline().split()))

            if animal[0] == "what":
                print(" ".join(sound))
                break

            while animal[2] in sound:
                sound.remove(animal[2])

if __name__ == "__main__":
    main()
