package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here

     System.out.print(keepRolling());
    }

    public static int rollDice(int Sides){

        double randomNumber = Math.random();

        randomNumber *=Sides;
        randomNumber +=1;

        return (int) randomNumber;

    }

    public static String Googol(){

        String googol = "1";

        int len = googol.length();

        while(len < 101){

            googol = googol + "0";
            len = googol.length();

            System.out.print(googol);
        }

        return googol;
    }

    //============================================//
    // this function play a yetcee               //
    //==========================================//

    public static int keepRolling(){

        int dice1 = rollDice(0);
        int dice2 = rollDice(0);
        int count = 1;

        while(!(dice1 == dice2)){

            dice1 = rollDice(0);
            dice2 = rollDice(0);
            count = count +1;
        }

        return count;
    }
}
