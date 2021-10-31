import java.util.*;
class MaximumSumOfSubArray{
    public static void main(String []args){
        int[] Array = {1,2,3,4,5,6,7,8,9,10,11,12};
        int window = 3;
        int sum = 0;
        int max = Integer.MIN_VALUE;
        for (int i = 0,j = 0; j < Array.length;j++){
            sum += Array[j];
            if(i+j+1 > window){
                sum -= Array[i++];
                max = max > sum ? max : sum; // Replace > with '<' for Minimum Sum of a subarray with fixed window.
            }
        }
        System.out.println(max);
    }
}