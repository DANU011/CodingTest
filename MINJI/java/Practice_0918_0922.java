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
