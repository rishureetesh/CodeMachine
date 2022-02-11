import java.util.ArrayList;
import java.util.List;

public class MaxAreaHistogram {
    public static int[] nextGreaterToRight(int[] array){
        int[] leftArray = new int[array.length];
        return leftArray;
    }
    public static int[] nextGreaterToLeft(int[] array){
        int[] rightrArray = new int[array.length];
        for(int i)
        return rightrArray;
    }
    public static int getMaxArea(int[] array){
        List<Integer> list=new ArrayList<Integer>();
        int[] leftMax = nextGreaterToLeft(array);
        int[] rightMax = nextGreaterToRight(array);
        for(int i=0;i<array.length;i++){
        }
        return 0;
    }
    public static void main(String[] args) {
        int[] array={6,2,5,4,5,1,6};
        System.out.println(getMaxArea(array));
    }
}
