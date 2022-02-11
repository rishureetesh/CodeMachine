import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class StockSpan{
    static class Node{
        int index, value;
        public Node(int index, int value){
            this.index=index;
            this.value=value;
        }
    }
    static public List<Integer> getStockSpan(int[] array){
        Stack<Node> stack=new Stack<Node>();
        List<Integer> result=new ArrayList<Integer>();
        for(int i=0;i<array.length;i++){
            if(stack.empty() || stack.peek().value > array[i]){
                result.add(1);
            }else{
                while(!stack.empty() && stack.peek().value <= array[i]) stack.pop();
                if(stack.empty()){
                    result.add(i);
                }else{
                    result.add(i-stack.peek().index);
                }
            }
            stack.push(new Node(i, array[i]));
        }
        return result;
    }
    public static void main(String[] args) {
        int[] array = {100,80,60,70,60,75,85};
        System.out.println(getStockSpan(array));
    }
}