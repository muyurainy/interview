package study;

import java.util.Arrays;

public class sort {
    public static void main(String[] args){
        int[] a = {3, 2, 5, 4, 1};
        int[] tmp = {3, 2, 5, 4, 1};
        QuickSort qsort = new QuickSort();
        qsort.sort(a, 0, a.length-1);
        System.out.println("QuickSort: \n" + Arrays.toString(a));
        for (int i = 0; i< a.length; i++)
            a[i] = tmp[i];
        BubbleSort bsort = new BubbleSort();
        bsort.sort(a);
        System.out.println("BubbleSort: \n" + Arrays.toString(a));
        SelectionSort ssort = new SelectionSort();
        ssort.sort(a);
        System.out.println("SelectionSort: \n" + Arrays.toString(a));
        InsertionSort isort = new InsertionSort();
        isort.sort(a);
        System.out.println("InsertionSort: \n" + Arrays.toString(a));
        String s = "abc";
        s = "abcd";
        System.out.println(s);
    }
}

class sort_base {
    public void swap(int a[], int i, int j){
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
}

class QuickSort extends sort_base{
    int partition(int[] a, int l, int h){
        int i = l, j = h+1;
        int tmp = a[i];
        while (true){
            while (a[++i] < tmp && i!= h);
            while (a[--j] > tmp && j!= l);
            if (i >= j)
                break;
            swap(a, i, j);
        }
        swap(a, l, j);
        return j;
    }
    void sort(int a[],int l,int h){
        if ( h <= l)
            return;
        int j = partition(a, l, h);
        sort(a, l, j-1);
        sort(a, j+1, h);
    }
}

class BubbleSort extends sort_base{
    void sort(int a[]) {
        boolean hasSort = false;
        for (int i = a.length - 1; i > 0 && !hasSort; i--) {
            hasSort = true;
            for (int j = 0; j < i; j++) {
                if (a[j] > a[j+1]){
                    hasSort = false;
                    swap(a, j, j+1);
                }
            }
        }
    }
}

class SelectionSort extends sort_base{
    void sort(int a[]){
        for (int i = 0; i < a.length - 1; i++){
            int min = i;
            for (int j = i; j < a.length; j++){
                if (a[j] < a[min])
                    min = j;
            }
            swap(a, i, min);
        }
    }
}

class InsertionSort extends sort_base{
    void sort(int[] a){
        for (int i = 1; i < a.length; i++)
            for (int j = i; j > 0 && a[j] < a[j-1]; j--)
                swap(a, j-1, j);
    }
}