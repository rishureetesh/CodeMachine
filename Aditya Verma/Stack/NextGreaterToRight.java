import java.util.Stack;
class NextGreaterToRight {
    class Node{
        int temperature,index;
        public Node(int temperature, int index){
            this.temperature=temperature;
            this.index=index;
        }
    }
    public int[] dailyTemperatures(int[] temperatures) {
        int holdResult[] = new int[temperatures.length];
        Stack<Node> stack=new Stack<Node>();
        for(int i=temperatures.length-1;i>=0;i--){
            if(stack.empty()){
                holdResult[i]=0;
            }else if(!stack.empty() && stack.peek().temperature > temperatures[i]){
                holdResult[i]=stack.peek().index-i;
            }else{
                while(!stack.empty() && stack.peek().temperature <= temperatures[i]) stack.pop();
                if(stack.empty()){
                    holdResult[i]=0;
                }else{
                    holdResult[i] = stack.peek().index-i;
                }
            }
            stack.push(new Node(temperatures[i],i));
        }
        return holdResult;
    }
    public static void main(String[] args){
        int array[]={73,74,75,71,69,72,76,73};
        NextGreaterToRight obj=new NextGreaterToRight();
        int returnedArray[] = obj.dailyTemperatures(array);
        for(int data:returnedArray){
            System.out.println(data);
        }
    }
}