package study;

public class jichu {
}

class overload{
    static private String func(String name, int age){
        System.out.println("Hi " + name + ", your age is: " + age);
        return name;
    }
    static private int func1(String name, int age){
        System.out.println("return your age");
        return age;
    }
    static class A {
        public String a = "this is the class of A";
        public String show(D obj) {
            return ("A and D");
        }

        public String show(A obj) {
            return ("A and A");
        }
    }

    static class B extends A {
        public String name = "hello";
        public String show(B obj) {
            return ("B and B");
        }

        public String show(A obj) {
            return ("B and A");
        }
    }

    static class C extends B {
    }

    static class D extends B {
    }
    public static void main(String[] args){
        func("lcy", 18);
        A a1 = new A();
        A a2 = new B();
        B b = new B();
        //B b1 = new A();
        C c = new C();
        D d = new D();
        System.out.println(a1.show(b)); // A and A
        System.out.println(a1.show(c)); // A and A
        System.out.println(a1.show(d)); // A and D
        System.out.println(a2.show(b)); // B and A
        System.out.println(a2.show(c)); // B and A
        System.out.println(a2.show(d)); // A and D
        System.out.println(b.show(b));  // B and B
        System.out.println(b.show(c));  // B and B
        System.out.println(b.show(d));  // A and D
        //System.out.println(a2.a + a2.name);
    }
}