import java.util.*;
class FloorElement{
    static int floorElement(int[] Array, int low, int high , int Element){
        if (low > high){
            return -1;
        }
        int mid = (high + low) / 2;
        if (Array[mid] < Element){
            if(mid+1 <= high && Array[mid+1] < Element){
                return floorElement(Array, mid+1, high, Element);
            }else{
                return Array[mid];
            }
        }else{
            return floorElement(Array, low, mid-1, Element);
        }
    }
    public static void main(String[] args){
        int[] Array = {1,2,3,4,7,8,9};
        int index = floorElement(Array, 0, Array.length-1, 12);
        if (index == -1){
            System.out.println("Floor element for the mentioned doesn't exists :(");
        }else{
            System.out.println("Floor element for the mentioned is " + index);
        }
    }
}