package com.company;

public class Main {

    public static void main(String[] args) {
        // write your code here
//        System.out.print(maxi(32,23));
        double [] arrays = {32,3,25,6,2,6,232,};
        System.out.println(findSmallestNum(arrays));
    }

    private static int maxi(int i, int i1) {

        int result = 0;

        if (i < i1) {
            result = i;
        } else {
            result = i1;
        }

        return result;
    }
    private static double maxi(double i, double i1){
        double result = 0;

        if(i < i1){
            result = i;
        }else {
            result = i1;
        }
        return result;
    }


    public static double findSmallestNum(double [] numbers){

        int size = numbers.length;
        int lucky = (int) size;
        double min = numbers[0];
        double total =0;
        for (int i =1; i< size; i++){

            if(numbers[i]<min){
                min = numbers[i];
            }
        }
        return min;
    }
}
