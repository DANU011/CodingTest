def count_segments(datas, splitter):
    
    return len([v for v in datas.split(splitter) if v])

def solution(datas):
    
    r_segments = count_segments(datas, "B")
    b_segments = count_segments(datas, "R")

    return min(r_segments + 1, b_segments + 1)

def main():
   
    N = int(input()) 
    datas = input().rstrip()
    
    print(solution(datas))
    
if __name__ == "__main__":
    main()    
