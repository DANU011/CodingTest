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

// 서울에서 김서방 찾기
class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        for(int i = 0; i < seoul.length; i++) {
            if(seoul[i].equals("Kim")) {
                answer = "김서방은 " + i + "에 있다";
            }
        }
        return answer;
    }
}

// 나누어 떨어지는 숫자 배열
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = Arrays.stream(arr)
                            .filter(x -> x % divisor == 0)
                            .sorted()
                            .toArray();

        return (answer.length == 0) ? new int[]{-1} : answer;
    }
}

// 음양 더하기
class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        for (int i = 0; i < absolutes.length; i++) {
            if (!signs[i]) absolutes[i] = -absolutes[i];
            answer += absolutes[i];
        }
        return answer;
    }
}

// 핸드폰 번호 가리기
class Solution {
    public String solution(String phone_number) {
        int length = phone_number.length();
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < length - 4; i++) {
            answer.append('*');
        }
        answer.append(phone_number.substring(length - 4));
        return answer.toString();
    }
}

// 없는 숫자 더하기
class Solution {
    public int solution(int[] numbers) {
        int sum = 45;
        for (int i : numbers) {
            sum -= i;
        }
        return sum;
    }
}

// 제일 작은 수 제거하기
class Solution {
    public int[] solution(int[] arr) {
        if(arr.length == 1){
            int[] answer = {-1};
            return answer;
        }
        int[] answer = new int[arr.length-1];
        int min = arr[0];
        for(int i = 0; i < arr.length; i++) {
            min = Math.min(min, arr[i]);
        }
        int index = 0;
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] == min) {
                continue;
            }
            answer[index++] = arr[i];
        }
        return answer;
    }
}
