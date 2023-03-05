package coding_test;

public class 짝수의합 {

	int Mysolution(int n) {
	    int answer = 0;
	    for (int i = 1; i <= n; i++) {
				if (i % 2 == 0) { 
					answer += i;
				}
			}
	    return answer;
	}
	
	int solution(int n) {
	    int answer = 0;
	    for (int i = 2; i <= n; i += 2) {
	        answer += i;
	    }
	    return answer;
	}
}
