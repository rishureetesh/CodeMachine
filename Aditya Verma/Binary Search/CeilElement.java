import java.util.*;
class CeilElement{
    static int ceilElement(int[] Array, int low, int high , int Element){
        if (low > high){
            return -1;
        }
        int mid = (high + low) / 2;
        if (Array[mid] > Element){
            if(mid > low && Array[mid-1] > Element){
                return ceilElement(Array, low, mid-1, Element);
            }else{
                return Array[mid];
            }
        }else{
            return ceilElement(Array, mid+1, high, Element);
        }
    }
    public static void main(String[] args){
        int[] Array = {1,2,3,4,7,8,9};
        int index = ceilElement(Array, 0, Array.length-1, 5);
        if (index == -1){
            System.out.println("Ceil element for the mentioned doesn't exists :(");
        }else{
            System.out.println("Floor element for the mentioned is " + index);
        }
    }
}