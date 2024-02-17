package day9;

import java.util.Scanner;

public class BOJ10807 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        int x = sc.nextInt();
        int result = 0;
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] == x) {
                result++;
            }
        }
        System.out.println(result);
    }
}