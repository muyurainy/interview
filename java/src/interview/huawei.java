package interview;

import java.util.*;
class Test {
    /*
    路径规划，直接暴力做的
     */
    private static int times = 0;
    private static int minCost = Integer.MAX_VALUE;
 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Deque <Node> queue = new LinkedList<>();
        int N = 5;
        boolean[] mark = new boolean[N];
        Node[] nodes = new Node[N];
        for (int i = 0; i < N; i ++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            nodes[i] = new Node(x, y);
        }
        //System.out.println(nodes[4].y);
        for (int tmp = 0; tmp<N; tmp++)
            mark[tmp] = false;
        for (int i = 0; i < N; i++){
            mark[i] = true;
            queue.add(nodes[i]);
            for (int j = 0; j<N; j++){
                if (mark[j])
                    continue;
                mark[j] = true;
                queue.add(nodes[j]);
                for (int k = 0; k<N; k++){
                    if (mark[k])
                        continue;
                    mark[k] = true;
                    queue.add(nodes[k]);
                    for (int m = 0; m < N; m++){
                        if (mark[m])
                            continue;
                        mark[m] = true;
                        queue.add(nodes[m]);
                        for (int n=0; n < N; n++){
                            if (mark[n])
                                continue;
                            mark[n] = true;
                            queue.add(nodes[n]);
                            int cur_cost = cal(queue);
                            //System.out.println(cur_cost);
                            //System.out.printf("%d, %d, %d, %d, %d\n", i, j, k, m, n);
                            minCost = minCost>cur_cost?cur_cost:minCost;
                            queue.removeLast();
                            mark[n] = false;
                        }
                        queue.removeLast();
                        mark[m] = false;
                    }
                    queue.removeLast();
                    mark[k] = false;
                }
                queue.removeLast();
                mark[j] = false;
            }
            queue.removeLast();
            mark[i] = false;
        }
        System.out.println(minCost);
        //permu(nodes, 0, minCost);
    }

    public static int cal(Deque queue){
        //Node list[] = new Node[5];
        double cal = 0.0;
        Iterator<Node> iter = queue.iterator();
        Node tmp = iter.next();
        cal += tmp.dis(0, 0);
        for(; iter.hasNext();){
            Node now = iter.next();
            cal += now.dis(tmp.x, tmp.y);
            tmp = now;
        }
        for(Iterator<Node> i = queue.iterator(); i.hasNext();){
            Node i_tmp = i.next();
            //System.out.printf("(%d, %d) ", i_tmp.x, i_tmp.y);
        }
        //System.out.print("\n");
        cal += tmp.dis(0, 0);
        
            //cal += list[i].dis(iter.n[i-1].x, list[i-1].y);
        return (int)cal;
    }
 
    private static class Node {
        public int x;
        public int y;
        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
        public double dis(int x, int y){
            return Math.sqrt(Math.pow(this.x-x, 2.0) + Math.pow(this.y-y, 2.0));
        }
    }
}