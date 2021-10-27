import java.util.*;
class BitonicArray{
    static int bitonicArray(int[] Array, int low, int high){
        if(low > high){
            return -1;
        }
        int mid = (low + high) / 2;
        int next = (mid + 1) % Array.length;
        int prev = (mid + Array.length - 1) % Array.length;
        if(Array[mid] > Array[prev] && Array[mid] > Array[next]){
            return Array[mid];
        }else if(Array[mid] < Array[next]){
            return bitonicArray(Array, mid+1, high);
        }else{
            return bitonicArray(Array, low, mid-1);
        }
    }
    public static void main(String []args){
        int[] Array = {1,2,3,4,9,8};
        int index = bitonicArray(Array, 0, Array.length-1);
        System.out.println("Element at peek : "+index);
    }
}