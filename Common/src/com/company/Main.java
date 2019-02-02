package com.company;

import java.util.Scanner;

public class Main {

   private static Scanner biNum = new Scanner(System.in);
   double deciNum;
   private static int binary;

    public static void main(String[] args) {
	// write your code here

        String toBinary = "Please Enter a binary number";
        System.out.println(toBinary);


        binary();

    }

    private static void binary() {

        double biToDec = 0;
        int call = biNum.nextInt();
        int decimal =0;
        int p = 0;
        int c = call;

      while(call !=0){

            biToDec = decimal +=((call%10)*Math.pow(2,p));
            call = call/10;
            p++;



        }

        System.out.println("THE BINARY  OF "+ c +" IS "+ biToDec +" IN DECIMAL");

    }
}
