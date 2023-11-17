// 둘만의 암호
class Solution {
    public String solution(String s, String skip, int index) {
       char[] words = s.toCharArray();
        for(int i = 0 ; i < words.length ; i++){
            for(int j = 0 ; j < index ; j++){
                do{
                    words[i]++;
                    if(words[i] > 'z'){
                        words[i] -= 26;
                    }
                }while(skip.contains(String.valueOf(words[i])));
            }
        }
        String answer = String.valueOf(words);
        return answer;
    }
}

// 크레인 인형뽑기 게임
import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        for(int move : moves) {
          for(int j = 0; j < board.length; j++) {
            if(board[j][move - 1] != 0) {
              if(stack.peek() == board[j][move - 1]) {
                stack.pop();
                answer += 2;
              } else {
               stack.push(board[j][move - 1]);
              }
              board[j][move - 1] = 0;
              break;
            }
          }
        }
        return answer;
    }
}

// 키패드 누르기
import java.util.*;

class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int left = 10;
        int right = 12;
        for(int num : numbers) {
            if(num == 1 || num == 4 || num == 7) {
                left = num;
                answer += "L";
            } else if(num == 3 || num == 6 || num == 9) {
                right = num;
                answer += "R";
            } else {
                if(num == 0) {
                    num = 11;
                }
                
                int leftDist = Math.abs(num-left) / 3 + Math.abs(num - left) % 3;
                int rightDist = Math.abs(num-right) / 3 + Math.abs(num - right) % 3;
                
                if(leftDist < rightDist) {
                    answer += "L";
                    left = num;
                } else if(leftDist > rightDist) {
                    answer += "R";
                    right = num;
                } else {
                    if(hand.equals("left")) {
                        answer += "L";
                        left = num;
                    } else {
                        answer +="R";
                        right = num;
                    }
                }
            }
        }
        return answer;
    }
}

// 햄버거 만들기
import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
       int answer = 0;
		List<Integer> li = new ArrayList<>();
		for(int i : ingredient) {
			li.add(i);
			while(li.size() >= 4) {
				int n = li.size();
				if(!(li.get(n - 1) == 1
					&& li.get(n - 2) == 3
					&& li.get(n - 3) == 2
					&& li.get(n - 4) == 1)) break;
				for(int j = 0; j < 4; j++) {
					li.remove(li.size() - 1);
				}
				answer++;
			}
		}
        return answer;
    }
}
