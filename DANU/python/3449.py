# 두 이진수 문자열 해밍거리 계산 hamming_distance
# 입력 받아서 결과 출력 main
def hamming_distance(bi_num1, bi_num2):
    dist = 0
    ## 거리 계산
    # 두 이진수 각 비트 비교
    # 같은 인덱스에 위치한 비트가 서로 다르면 증가
    for i in range(len(bi_num1)):
        if bi_num1[i] != bi_num2[i]:
            dist += 1
    return dist

def main():
    n = int(input())
    for _ in range(n):
        bi_num1 = input()
        bi_num2 = input()
        distance = hamming_distance(bi_num1, bi_num2)
        # print(f"\nHamming distance is {distance}.")
        # 터미널에서 씹힌거 여기서는 확인되지만 백준에서는 출력 형식이 잘못됐다고 나옴.
        # 라스트에 넣어서 확인하는 방식 고려
        print(f"Hamming distance is {distance}.")


if __name__ == "__main__":
    main()
