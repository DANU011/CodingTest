class Solution {
  public String solution(String my_string) {
      String answer = "";
      for (int i = my_string.length() - 1; i >= 0; i--) {
          answer = answer + my_string.charAt(i);
      }
      return answer;
  }
}

/*
class Solution {
  public String solution(String my_string) {
      StringBuffer sb = new StringBuffer(my_string);
      String reverse = sb.reverse().toString();
      return reverse;
  }
}
*/