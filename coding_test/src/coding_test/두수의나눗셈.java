package coding_test;

public class 두수의나눗셈 {

	int Mysolution(int num1, int num2) {
	    int answer = 0;
	    float a = (float) num1 / num2 * 1000;
	    answer = (int) a;
	    return answer;
	}
	
	int solution(int num1, int num2) {
	    int answer = 0;
	    answer = 1000*num1 / num2;
	    return answer;
	}
}
