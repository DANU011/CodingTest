// 가운데 글자 가져오기
class Solution {
    public String solution(String s) {
        String answer = "";
        int length = s.length();
        if(length % 2 == 0) {
            answer = s.substring(length/2-1, length/2+1);
        } else {
            answer = s.substring(length/2, length/2+1);
        }
        return answer;
    }
}

// 수박수박수박수박수박수?
class Solution {
    public String solution(int n) {
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < n; i++) {
            answer.append((i % 2 == 0) ? "수" : "박");
        }
        return answer.toString();
    }
}

// 내적
class Solution {
    public int solution(int[] a, int[] b) {
        int answer = 0;
        for(int i = 0; i < a.length; i++) {
            answer += a[i] * b[i];
        }
        return answer;
    }
}

// 약수의 개수와 덧셈
class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for(int i = left; i <= right; i++){
            int cnt = 0;
            for(int j = 1; j <= i; j++){
                if(i % j == 0) cnt++;
            }
            answer = (cnt % 2 == 0) ? answer + i : answer - i;
        }
        return answer;
    }
}
