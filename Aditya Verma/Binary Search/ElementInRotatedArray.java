import java.util.*;
class ElementInRotatedArray{
    static int elementInRotatedArray(int[] Array, int low, int high, int Element){
        if(low > high){
            return -1;
        }
        int mid = (low + high) / 2;
        if(Array[mid] == Element){
            return mid;
        }else if(Array[mid] > Element){
            return elementInRotatedArray(Array, low, mid-1, Element);
        }else{
            return elementInRotatedArray(Array, mid+1, high, Element);
        }
    }
    public static void main(String[] args){
        int[] Array = {5,6,7,8,9,10,11,12,13,14,1,2,3,4};
        int low = 0;
        int high = Array.length - 1;
        int index = RotatedArray.rotatedArray(Array, low, high);
        int Element = 4;
        System.out.println("Index : "+index);
        if(Array[index]<= Element && Array[high]>= Element){
            low = index;
        }else{
            high = (index + high) % Array.length;
        }
        int rotatedPosition = elementInRotatedArray(Array, low, high,Element);
        System.out.println("Elemnt found out at position : "+rotatedPosition);
    }
}