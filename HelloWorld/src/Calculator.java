import java.util.Scanner;

public class Calculator {

    public static String askOne = "Enter first number";
    public static String askTwo = "Enter second number";
    public static Scanner scanner;
    public static int num1 = 0;
    public static int num2 = 0;
    public static int ans = 0;
    public static  String question = null;


    public static void main(String [] args){



        String choice = " What do you want to do ?";
        String options = " For Addition [a], Subtraction [s], Multiplication [m]";
        String des = "+===============================================================+";

        int num1 = 0;
        int num2 = 0;


        System.out.println(choice);
        System.out.println(options);
        System.out.println(des);
        System.out.println();
        scanner = new Scanner(System.in);
        question = scanner.nextLine();

        if(question.equals("a")){

            //===============================================//
            // ask the user to enter first and second number//
            //=============================================//

           System.out.print(add(num1,num2));
        }

        else if(question.equals("s")){
            System.out.print(sub(num1,num2));
        }


        else if(question.equals("d")){
           System.out.print(div(num1,num2));
        }
        else if(question.equals("m")){


            System.out.print(mul(num1,num2));
        }


    }


    public static int add(int a, int b){

        System.out.print(askOne);
        num1 = scanner.nextInt();

        System.out.print(askTwo);
        num2 = scanner.nextInt();

        ans = num1 + num2;

        return ans ;
    }

    public static int sub(int a, int b){

        System.out.print(askOne);
        num1 = scanner.nextInt();

        System.out.print(askTwo);
        num2 = scanner.nextInt();

        ans = num1 - num2;

        return ans ;
    }

    public static int mul(int a, int b){
        System.out.print(askOne);
        num1 = scanner.nextInt();

        System.out.print(askTwo);
        num2 = scanner.nextInt();

        ans = num1 * num2;

        return ans ;
    }

    public static int div(int a, int b){
        System.out.print(askOne);
        num1 = scanner.nextInt();

        System.out.print(askTwo);
        num2 = scanner.nextInt();

        ans = num1 / num2;

        return ans ;
    }
}
