class Solution {
    boolean solution(String s) {
        int p = 0;
        int y = 0;
        boolean answer = true;
        
        // 전부 소문자로 변경
        String arr = s.toLowerCase();
        
        // p와 y 개수 세기
        for (int i = 0; i < arr.length(); i++) {
            char c = arr.charAt(i);
            if (c == 'p') {
                p++;
            }
            else if (c == 'y') {
                y++;
            }
        }
        answer = p == y? true : false;
        return answer;

        
    }
}