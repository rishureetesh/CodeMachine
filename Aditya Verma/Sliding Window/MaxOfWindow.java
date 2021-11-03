import java.util.*;
class MaxOfWindow{
    public static void main(String[] args){
        int[] Array = {1,-1,8,-8,7,6,2,3,-8,9,0};
        LinkedList<Integer> list = new LinkedList<Integer>();
        int window = 3;
        for(int j=0,i=0; j<Array.length; j++){
            while(list.size()>0 && list.getLast() < Array[j]){
                list.removeLast();
            }
            list.addLast(Array[j]);
            if(j-i+1 == window){
                System.out.println(list.getFirst());
                if(Array[i] == list.getFirst()){
                    list.removeFirst();
                }
                i++;
            }
        }
    }
}