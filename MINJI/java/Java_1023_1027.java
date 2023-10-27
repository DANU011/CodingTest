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

// 소수 찾기
class Solution {
    public int solution(int n) {
      int answer = 0; 
      boolean[] prime = new boolean[n + 1]; 
      for(int i = 2; i <= n; i++) 
      prime[i] = true;
      int root = (int)Math.sqrt(n); 
      for(int i = 2; i <= root; i++){
      if(prime[i] == true) {
      	 for(int j = i; i * j <= n; j++)
             prime[i * j] = false; 
         } 
      } 
      for(int i = 2; i <= n; i++) { 
      if(prime[i] == true)
         answer++; 
      } 
      return answer; 
    }
}

// 기사단원의 무기
class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for(int i = 1; i <= number; i++){
            int cnt = 0;
            for(int j = 1; j * j <= i; j++){
                if(j * j == i) cnt++;
                else if(i % j == 0) cnt += 2;
            }
            if(cnt > limit) cnt = power;
            answer += cnt;
        }
        return answer;
    }
}

// 덧칠하기
class Solution {
    public int solution(int n, int m, int[] section) {
        int roller = section[0];
        int cnt = 1;
        for(int i = 1; i < section.length; i++) {
            if(roller + m - 1 < section[i]) {
                cnt++;
                roller = section[i];
            }
        }
        return cnt;
    }
}

// 실패율
import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int noclear = 0;
        int player = stages.length;
        Map<Integer, Double> stagefail = new HashMap<Integer, Double>();
        for(int i = 1; i <= N; i++) {
            for(int s : stages){
                if(s == i) noclear++;
            }
            if(player == 0) stagefail.put(i, 0.0);
            else {
                stagefail.put(i, (double) noclear / player);
                player -= noclear;
                noclear = 0;
            }
        }
        List<Map.Entry<Integer, Double>> list_entries = new ArrayList<Map.Entry<Integer, Double>>(stagefail.entrySet());
        Collections.sort(list_entries, new Comparator<Map.Entry<Integer, Double>>() {
            public int compare(Map.Entry<Integer, Double> obj1, Map.Entry<Integer, Double> obj2) {
                return obj2.getValue().compareTo(obj1.getValue());
            }
        });
        int c = 0;
        for(Map.Entry<Integer, Double> entry : list_entries) {
            answer[c] = entry.getKey(); c++;
        }
        return answer;
    }
}
