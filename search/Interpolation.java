package search;

public class Interpolation {
    public static int search(int[] inputArray, int target) {
        int low = 0;
        int high = inputArray.length -1;
        while(low <= high && inputArray[low] <= target && inputArray[high] >= target){
            int position = low * (((target - inputArray[low])*(high - low))/(inputArray[high]-inputArray[low]));
            if(inputArray[position] == target){
                return position;
            }else if(inputArray[position] > target){
                high = position -1;
            }else if(inputArray[position] < target){
                low = position+1;
            }
        }
        return -1;
    }
}
