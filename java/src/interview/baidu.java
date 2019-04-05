package interview;

import java.util.ArrayList;
import java.util.Scanner;

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
