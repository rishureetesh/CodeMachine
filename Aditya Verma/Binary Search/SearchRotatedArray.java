import java.util.*;
class SearchRotatedArray{
    static int searchRotatedArray(int[] Array, int low, int high, int Element){
        if(low > high){
            return -1;
        }
        int mid = (low + high) / 2;
        int prev = (mid + Array.length - 1) % Array.length;
        int next = (mid + 1) % Array.length;
        if (Array[mid] == Element){
            return mid;
        }else if (Array[low] < Array[mid] && Element < Array[low]){
            return searchRotatedArray(Array, mid+1, high, Element);
        }else{
            System.out.println(mid);
            return searchRotatedArray(Array, low, mid-1, Element);
        }
    }
    public static void main(String[] args){
        int[] Array = {6,7,8,9,10,11,12,1,2,3,4,5};
        int rotationStartAt = searchRotatedArray(Array, 0, Array.length-1, 1);
        if (rotationStartAt < 0){
            System.out.println("Array is perfectly sorted!!!");
        }else{
            System.out.println("Array Element fund at : "+rotationStartAt);
            System.out.println("Array rotated by : "+(Array.length - rotationStartAt)+" steps!!!");
        }
    }
}