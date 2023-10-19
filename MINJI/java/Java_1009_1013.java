// 가장 가까운 같은 글자
class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
			for (int j = i; j >= 0; j--) {
				if (s.charAt(i) == s.charAt(j) && answer[i] == 0) {
					answer[i] = i - j;
				}
			}
			if (answer[i] == 0) {
				answer[i] = -1;
			}
		}
        return answer;
    }
}

// 비밀지도
class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        String temp;
        for(int i = 0 ; i < n ; i++){
            temp = String.format("%16s", Integer.toBinaryString(arr1[i] | arr2[i]));
            temp = temp.substring(temp.length() - n);
            temp = temp.replaceAll("1", "#");
            temp = temp.replaceAll("0", " ");
            answer[i] = temp;
        }
        return answer;
    }
}

// K번째수
import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int i = 0; i < commands.length; i++){
            int[] temp = Arrays.copyOfRange(array, commands[i][0] - 1, commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2] - 1];
        }
        return answer;
    }
}

// 푸드 파이트 대회
class Solution {
    public String solution(int[] food) {
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < food.length; i++) {
            int count = food[i] / 2;
            sb.append(String.valueOf(i).repeat(count));
        }
        String answer = sb + "0";
        answer += sb.reverse();
        return answer;
    }
}

// 두 개 뽑아서 더하기
import java.util.HashSet;

class Solution {
   public int[] solution(int[] numbers) {
	   HashSet<Integer> hs = new HashSet<>();
       for(int i = 0; i < numbers.length - 1; i++){
           for(int j = i + 1; j < numbers.length; j++){
               hs.add(numbers[i] + numbers[j]);
           }
       }
       return hs.stream().mapToInt(Integer::intValue).sorted().toArray();
    }
}

// 콜라 문제
class Solution {
    public int solution(int a, int b, int n) {
        int count = 0;
        while(n >= a) {
            count += n / a * b;
            n = n / a * b + n % a;
        }
		return count;
    }
}

// 추억 점수
import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        for(int i = 0; i < photo.length; i++){
            for(int j = 0; j < photo[i].length; j++){
                if(Arrays.asList(name).indexOf(photo[i][j]) != -1){
                    answer[i] += yearning[Arrays.asList(name).indexOf(photo[i][j])];
                }
            }
        }
        return answer;
    }
}

// 명예의 전당 (1)
import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        List<Integer> sc = new ArrayList();
        for (int i = 0; i < score.length; i++) {
            if (i < k - 1){
                sc.add(score[i]);
                sc.sort(Collections.reverseOrder());
                answer[i] = sc.get(sc.size() - 1);
            } else if (i >= k - 1){
                sc.add(score[i]);
                sc.sort(Collections.reverseOrder());
                answer[i] = sc.get(k - 1);
            }
        }
        return answer;
    }
}
