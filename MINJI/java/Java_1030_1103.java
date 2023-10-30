// [1차] 다트 게임
class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        String[] dart = dartResult.split("");
        int[] score = new int[3];
        int index = -1;
        for(int i = 0; i < dart.length; i++) {
            if(dart[i].matches("[0-9]")) {
                index++;
                score[index] = Integer.parseInt(dart[i]);
                if(dart[i+1].matches("[0-9]")) {
                    score[index] *= 10;
                    i++;
                }
            }
            switch(dart[i]) {
                case "D":
                    score[index] = (int)Math.pow(score[index], 2);
                    break;
                case "T" :
                    score[index] = (int)Math.pow(score[index], 3);
                    break;
                case "*" :
                    score[index] *= 2;
                    if(index - 1 >= 0) score[index-1] *= 2;
                    break;
                case "#" :
                    score[index] *= -1;
            }
        }
        for(int s : score) {
            answer += s;
        }
        return answer;
    }
}

// 옹알이 (2)
class Solution {
    public int solution(String[] babblings) {
        int answer = 0;
        for(int i = 0; i < babblings.length; i++) {
            if(babblings[i].contains("ayaaya") || babblings[i].contains("yeye") || babblings[i].contains("woowoo") || babblings[i].contains("mama")) {
                continue;
            }
            babblings[i] = babblings[i].replace("aya", " ");
            babblings[i] = babblings[i].replace("ye", " ");
            babblings[i] = babblings[i].replace("woo", " ");
            babblings[i] = babblings[i].replace("ma", " ");
            babblings[i] = babblings[i].replace(" ", "");
            if(babblings[i].length() == 0) answer++;
        }
        return answer;
    }
}
