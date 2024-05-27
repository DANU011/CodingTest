def find_minimum_number(nums: str) -> int:
    n = 0
    idx = 0
    while True:
        n += 1
        for s in str(n):
            if nums[idx] == s:
                idx += 1
                if idx >= len(nums):
                    return n

def main():
    import sys
    input = sys.stdin.read().strip()
    result = find_minimum_number(input)
    print(result)

if __name__ == "__main__":
    main()
