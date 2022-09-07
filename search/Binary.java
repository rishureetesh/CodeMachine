package search;
public class Binary{
    public static int search(int[] inputArray, int target) {
        return search(inputArray, target, 0, inputArray.length - 1);
    }
    public static int search(int[] inputArray, int target, int low, int high) {
        while(low <= high){
            int mid = low + (high - low)/2;
            if(inputArray[mid] == target){
                return mid;
            }else if(inputArray[mid] > target){
                high = mid -1;
            }else{
                low = mid+1;
            }
        }
        return -1;
    }
    public int[] search(int[][] inputArray, int target) {
        int low = 0;
        int high = inputArray[0].length -1;
        while(low<inputArray.length && high >= 0){
            if(inputArray[low][high] == target){
                return new int[]{low, high};
            }else if(inputArray[low][high] > target){
                high -= 1;
            }else{
                low += 1;
            }
        }
        return null;
    }
}