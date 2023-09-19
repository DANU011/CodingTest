// 정수 내림차순으로 배치하기
import java.util.*;
class Solution {
    public long solution(long n) {
        long answer = 0;
        String nString = Long.toString(n);
        String[] arr = new String[nString.length()];
        String result = "";
        for (int i = 0; i < nString.length(); i++) {
            arr[i] = nString.substring(i, i+1);
        }
        Arrays.sort(arr, Collections.reverseOrder());
        result = String.join("", arr);
        return Long.parseLong(result);
    }
}

import java.util.Arrays;
class Solution {
    public long solution(long n) {
        char[] arr = Long.toString(n).toCharArray();
        Arrays.sort(arr);
        return Long.parseLong(new StringBuilder(new String(arr)).reverse().toString());
    }
}

// 하샤드 수
class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int sum = 0;
        String[] num = Integer.toString(x).split("");
        for(int i = 0; i < num.length; i++) {
            sum += Integer.parseInt(num[i]);
        }
        if(x % sum != 0)
            answer = false;
        return answer;
    }
}

// 두 정수 사이의 합
class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int max = Math.max(a, b);
        int min = Math.min(a, b);
        for(int i = min ; i<=max; i++) {
            answer += i;
        }
        return answer;
    }
}

// 콜라츠 추측
class Solution {
    public int solution(long num) {
        int answer = 0;
        while(num != 1) {
            if(num % 2 == 0)
                num /= 2;
            else
                num = num * 3 + 1;
            answer++;
            
            if(answer >= 500) {
                answer = -1;
                break;
            }
        }
        return answer;
    }
}
