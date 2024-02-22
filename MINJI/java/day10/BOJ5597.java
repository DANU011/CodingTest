package day10;

import java.util.Scanner;

public class BOJ5597 {
    public static void main(String[] args) {
        int[] students = new int[31];
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < 28; i++) {
            int num = sc.nextInt();
            students[num]++;
        }
        for(int i = 1; i <= 30; i++) {
            if(students[i] == 0) System.out.println(i);
        }
    }
}
