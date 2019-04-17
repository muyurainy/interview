package interview;

import javafx.scene.input.DataFormat;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.*;
import java.text.DateFormat;
public class baidu {
}

class dfs_char{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        ArrayList<String> list = new ArrayList<>();
        for (String i : input.split(" ")){
            System.out.println(i);

        }
    }
}

class  pra{
    int[] i =new int [10];
    String name;
    void print()
    {
        System.out.println(i+"and"+name);
    }
    public static void main(String[] args){
        pra var = new pra();
        var.print();

    }
}

class  weizhong{
    public static void greet(){
        System.out.println("hello");
    }
    public static void main(String[] args){
        weizhong x = null;
        x.greet();
        ((weizhong) x).greet();
        ((weizhong) null).greet();
        DataFormat df;
        Date date = new Date();
    }
}

class  weizhong1{
    public static void count(int n,int m) {
        Queue<Integer> persons = new LinkedList<>();
        ArrayList<Integer> output = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            persons.add(i + 1);
        }
        int counts = 0;
        while (!persons.isEmpty()) {
            Integer person = persons.poll();
            counts++;
            if (counts % m == 0) {
                output.add(person);
            } else {
                persons.add(person);
            }
        }
        if (output.size()==1)
            System.out.println(output.get(0));
        else {
            System.out.printf("%d", output.get(0));
            for (int i = 1; i < output.size() - 1; i++)
                System.out.printf(" %d", output.get(i));

            System.out.printf("\n%d", output.get(output.size() - 1));
        }
    }

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int m = s.nextInt();
        count(n, m);
    }
}

class  weizhong2{

    public static void main(String[] args){
        //count(n, m);
        System.out.println( (3 * 10 / 3 ));
    }
}