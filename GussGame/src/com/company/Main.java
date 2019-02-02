package com.company;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Random;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {


        File file = new File("/home/koliko/Desktop/test.txt");

        Scanner scanner = new Scanner(file);

        System.out.print(scanner);
       scanner.close();

       File file1 = new java.io.File("/home/koliko/Desktop/test2.txt");

        PrintWriter printWriter = new PrintWriter(file1);

        printWriter.print("John monkey");

        printWriter.close();
    }
}
