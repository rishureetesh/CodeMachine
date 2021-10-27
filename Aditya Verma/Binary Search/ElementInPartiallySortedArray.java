import java.util.*;
class ElementInPartiallySortedArray{
    static int elementInPartiallySortedArray(int[] Array, int low, int high, int Element){
        if(low > high){
            return -1;
        }
        int mid = (low + high) / 2;
        if(Array[mid] == Element){
            return mid;
        }else if(mid < high && Array[mid+1] == Element){
            return mid + 1;
        }else if(mid > low && Array[mid-1] == Element){
            return mid - 1;
        }else if(Array[mid] > Element){
            return elementInPartiallySortedArray(Array, low, mid-1, Element);
        }else{
            return elementInPartiallySortedArray(Array, mid+1, high, Element);
        }
    }
    public static void main(String []args){
        int[] Array = {2,1,3,5,4,6,7,9,8};
        int index = elementInPartiallySortedArray(Array, 0, Array.length-1, 5);
        if (index < 0){
            System.out.println("Element not found!!!");
        }else{
            System.out.println("Element found at : "+index);
        }
    }
}