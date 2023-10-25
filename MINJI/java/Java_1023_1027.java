// 폰켓몬
import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int max = nums.length / 2;
        HashSet<Integer> numsSet = new HashSet<>();
        for (int num : nums) {
          numsSet.add(num);
        }
        if (numsSet.size() > max) {
          return max;
        } else {
          return numsSet.size();
        }
    }
}

// 과일 장수
import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        Arrays.sort(score);
        for(int i = score.length; i >= m; i -= m){
            answer += score[i - m] * m;
        }
        return answer;
    }
}

// 모의고사
import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] first = {1,2,3,4,5};
        int[] second = {2,1,2,3,2,4,2,5};
        int[] third = {3,3,1,1,2,2,4,4,5,5};
        int[] score = {0,0,0};
        for(int i = 0; i < answers.length; i++) {
            if(answers[i] == first[i%5]) score[0]++;
            if(answers[i] == second[i%8]) score[1]++;
            if(answers[i] == third[i%10]) score[2]++;
        }
        int max = Math.max(score[0], Math.max(score[1], score[2]));
        List<Integer> answ = new ArrayList<Integer>();
        for(int i = 0; i < score.length; i++) if(max == score[i]) answ.add(i + 1);
        int[] answer = new int[answ.size()];
        for(int i = 0; i < answ.size(); i++){
            answer[i] = answ.get(i);
        }
        return answer;
    }
}

// 소수 만들기
class Solution {
   public int solution(int[] nums) {
      int answer = 0;
      boolean chk = false;
      for (int i = 0; i < nums.length; i++) {
         for (int j = i + 1; j < nums.length; j++) {
            for (int k = j + 1; k < nums.length; k++) {
               int num = nums[i] + nums[j] + nums[k];
               if (num >= 2) chk = sosu(num);
               if (chk == true) answer++; 
            }
         }
      }
      return answer;
   }
    
   public boolean sosu(int num) {
      boolean check = true; 
      if(num==2) {
         return check;
      }
      for(int i=2; i<num; i++) {
         if(num%i ==0) {
            check = false;
            break;
         }
      }
      return check;
   }
}
