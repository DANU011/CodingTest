// 나머지가 1이 되는 수 찾기
class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i = 2; i < n; i++) {
            if(n % i == 1) {
                answer = i;
                break;
            }
        }
        return answer;
    }
}

// 평균 구하기
class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        double result = 0;
        for(int i = 0; i < arr.length; i++) {
            result += arr[i];
        }
        answer = result / arr.length;
        return answer;
    }
}

// 자릿수 더하기
import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        while(true){
            answer+=n%10;
            
            if(n<10) break;
            
            n=n/10;
        }
        return answer;
    }
}

// 짝수와 홀수
class Solution {
    public String solution(int num) {
        String answer = "";
        if(num % 2 == 0) {
            answer = "Even";
        } else {
            answer = "Odd";
        }
        return answer;
    }
}

// 약수의 합
class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i = 1; i < n + 1; i++) {
            if(n % i == 0) {
                answer += i;
            }
        }
        return answer;
    }
}

// x만큼 간격이 있는 n개의 숫자
class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        long num = x;
        for(int i = 0; i < answer.length; i++){
            answer[i] = num;
            num += x;
        }
        return answer;
    }
}

// 자연수 뒤집어 배열로 만들기
class Solution {
    public int[] solution(long n) {
        String a = "" + n;
        int[] answer = new int[a.length()];
        int cnt=0;
        while(n > 0) {
            answer[cnt]=(int)(n%10);
            n/=10;
            System.out.println(n);
            cnt++;
        }
        return answer;
    }
}

// 문자열을 정수로 바꾸기
class Solution {
    public int solution(String s) {
        return Integer.parseInt(s);
    }
}

// 문자열 내 p와 y의 개수
class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'p')
                count++;
            else if (s.charAt(i) == 'y')
                count--;
        }
        return count == 0;
    }
}

// 정수 제곱근 판별
class Solution {
    public long solution(long n) {
        if (Math.pow((int)Math.sqrt(n), 2) == n) {
            return (long) Math.pow(Math.sqrt(n) + 1, 2);
        }
        return -1;
    }
}
