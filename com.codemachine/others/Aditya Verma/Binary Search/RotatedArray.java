import java.util.*;
class RotatedArray{
    static int rotatedArray(int[] Array, int low, int high){
        if(low > high){
            return -1;
        }
        int mid = (low + high) / 2;
        int prev = (mid + Array.length - 1) % Array.length;
        int next = (mid + 1) % Array.length;
        if (Array[mid] < Array[prev] && Array[mid] < Array[next]){
            return mid;
        }else if (Array[mid] > Array[high]){
            return rotatedArray(Array, mid+1, high);
        }else{
            return rotatedArray(Array, low, mid-1);
        }
    }
    public static void main(String[] args){
        int[] Array = {1,2,3,4,5,6,7,8,9,10,11,12};
        int rotationStartAt = rotatedArray(Array, 0, Array.length-1);
        if (rotationStartAt <= 0){
            System.out.println("Array is perfectly sorted!!!");
        }else{
            System.out.println("Array rotated by : "+(Array.length - rotationStartAt)+" steps!!!");
        }
    }
}