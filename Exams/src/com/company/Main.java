package com.company;


public class Main {

    static int goArray [] = {1,4,9,16,25};
    static int moArray []={};
    public static void main(String[] args) {
	// write your code here

        fArray(goArray);
//        System.out.print(block);

    }

    private static void fArray(int[] minArray) {

        for(int i = 0; i < minArray.length; i++){

            int temp = minArray[i];
//            if(temp ==minArray.length-i){
//                int temps = goArray[temp];
//                int u = temps;
//                System.out.print(u);
//            }
            System.out.print(temp);
        }
    }


}
