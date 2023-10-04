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

// 문자열 내림차순으로 배치하기
import java.util.Arrays;
import java.util.Collections;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] str = s.split("");
        Arrays.sort(str, Collections.reverseOrder());
        for(String a : str)
           answer += a;
        return answer;
    }
}

// 부족한 금액 계산하기
class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        long total = 0;
        for(int i = 1; i < count + 1; i++){
            total += price * i;
        }
        if(money < total)
            answer = total - money;
        else
            answer = 0;
        return answer;
    }
}

// 문자열 다루기 기본
class Solution {
    public boolean solution(String s) {
        if(s.length() == 4 || s.length() == 6){
          try{
              int x = Integer.parseInt(s);
              return true;
          } catch(NumberFormatException e){
              return false;
          }
      }
      else return false;
    }
}

// 행렬의 덧셈
class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        for(int i = 0; i < arr1.length; i++) {
            for(int j = 0; j < arr1[0].length; j++) {
                arr1[i][j] += arr2[i][j];
            }
        }
        return arr1;
    }
}

// 직사각형 별찍기
import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int height = sc.nextInt();
        int width = sc.nextInt();
        String row = "*".repeat(width);
        for (int i = 0; i < height; i++) {
            System.out.println(row);
        }
    }
}

// 최대공약수와 최소공배수
import java.math.BigInteger;

class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        BigInteger bigN = BigInteger.valueOf(n);
        BigInteger bigM = BigInteger.valueOf(m);
        BigInteger gcd = bigN.gcd(bigM);
        BigInteger lcm = bigN.multiply(bigM).divide(gcd);
        answer[0] = gcd.intValue();
        answer[1] = lcm.intValue();
        return answer;
    }
}
