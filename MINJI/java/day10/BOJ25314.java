package day10;

import java.util.Scanner;

public class BOJ25314 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = n / 4;
        for(int i = 0; i < m; i++) {
            System.out.print("long ");
        }
        System.out.println("int");
    }
}
