import java.util.*;
import java.lang.Math;
class MinimumDifference{
    static int minimumDifference(int[] Array, int low, int high, int Element){
        if(low > high){
            if(high < 0){
                ++high;
            }
            if(low >= Array.length){
                --low;
            }
            if(Math.abs(Array[low] - Element) > Math.abs(Array[high] - Element)){
                return Array[high];
            }else{
                return Array[low];
            }
        }
        int mid = low + (high-low) / 2;
        if(Array[mid] == Element){
            return Array[mid];
        }else if(Element < Array[mid]){
            return minimumDifference(Array, low, mid-1, Element);
        }else{
            return minimumDifference(Array, mid+1, high, Element);
        }
    }
    public static void main(String[] args){
        int[] Array = {1,2,3,4,5,7,10};
        int data = minimumDifference(Array, 0, Array.length-1, 8);
        System.out.println(data);
    }
}