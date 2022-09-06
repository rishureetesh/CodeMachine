import java.util.*;
class CountOFOccurance{
    static int getTotalOccurance(int[] Array, int Low, int High, int Element, boolean Initial){
        if (Low > High)
            return -1;
        int Mid = (Low + High)/2;
        if (Array[Mid] == Element){
            if (Initial && Array[Mid-1] == Element && Mid-1 >= 0){
                return getTotalOccurance(Array,Low,Mid-1,Element,Initial);
            }else if(!Initial && Array[Mid+1] == Element && Mid+1 < Array.length){
                return getTotalOccurance(Array,Mid+1,High,Element,Initial);
            }else{
                return Mid;
            }
        }else if (Array[Mid] > Element){
            return getTotalOccurance(Array,Low,Mid-1,Element,Initial);
        }else{
            return getTotalOccurance(Array,Mid+1,High,Element,Initial);
        }
    }
    public static void main(String[] args){
        int [] Array = {2,3,4,5,6,7,8,9};
        int Initial = getTotalOccurance(Array,0,Array.length-1,6,true);
        if (Initial != -1){
            int Last = getTotalOccurance(Array,0,Array.length-1,6,false);
            int Calculation = Last - Initial + 1;
            System.out.println("Total Occurance of 6 is : "+Calculation);
        }else{
            System.out.println("Element not found");
        }
    }
}