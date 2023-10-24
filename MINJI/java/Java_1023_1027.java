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
