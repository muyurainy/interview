package interview;
//import java.util.*;

class version_compare{
    public static void main(String[] args){
        String a = new String("1.2");
        String b = "1.1456";
        String del = "\\.";
        String[] a_list = a.split(del);
        String[] b_list = b.split(del);
        for(String i: a_list)
            System.out.println(i);
        int a_z = Integer.parseInt(a_list[0]);
        int b_z = Integer.parseInt(b_list[0]);
        if (a_list[1].length() > b_list[1].length())
            for(int i = 0; i < a_list[1].length() - b_list[1].length(); i++)
                b_list[1] += '0';
        else
            for(int i = 0; i < b_list[1].length() - a_list[1].length(); i++)
                a_list[1] += '0';

        int a_x = Integer.parseInt(a_list[1]);
        int b_x = Integer.parseInt(b_list[1]);
        if (a_z>b_z)
            System.out.println("a>b");
        else if (a_z<b_z)
            System.out.println("a<b");
        else
        if (a_x > b_x)
            System.out.println("a>b");
        else if (a_x < b_x)
            System.out.println("a<b");
        else
            System.out.println("a=b");
    }
}

class print_star{
    static void print(int n){
        int length = n/2 + 1;
        for (int i=length; i > 0; i--){
            String first = muti_str(" ", length-i);
            String second = muti_str("*", 2*i-1);
            String thrid = muti_str(" ", length-i);
            System.out.println(first+second+thrid);
        }
    }
    public static void main(String[] args){
        print(5);
    }

    static String muti_str(String s, int n){
        String or = "";
        for (int i = 0; i < n; i++)
            or += s;
        return or;
    }
}

class Permutation{
    public static void main(String[] args){
        int n = 4;
        int[] list = new int[n];
        for (int i=1;i<=n;i++)
            list[i-1] = i;
        permutation(list, 3, 0);
    }
    private static void permutation(int[] list, int all, int begin){
        if (begin==all-1){
            for (int i=0;i<all;i++)
                System.out.printf("%d ", list[i]);
            System.out.print("\n");
        }
        for (int i = begin; i<list.length; i++){
            int tmp = list[begin];
            list[begin] = list[i];
            list[i] = tmp;
            permutation(list, all, begin+1);
            tmp = list[begin];
            list[begin] = list[i];
            list[i] = tmp;

        }
    }
}
