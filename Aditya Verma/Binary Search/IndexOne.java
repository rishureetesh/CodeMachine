import java.util.*;
class IndexOne{
    static int indexOne(int[] Array, int low, int high){
        if (low > high){
            return -1;
        }
        int mid = (high + low) / 2;
        if (Array[mid] == 1){
            if(mid-1 > 0){
                return indexOne(Array, low, mid-1);
            }else{
                return mid;
            }
        }else{
            return indexOne(Array, mid+1, high);
        }
    }
    public static void main(String[] args){
        int[] Array = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1};
        int index = indexOne(Array, 0, Array.length-1);
        if (index == -1){
            System.out.println("One cannot be searched in the given list :(");
        }else{
            System.out.println("First occurance at index " + index);
        }
    }
}