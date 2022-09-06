package java.template.search;
import java.lang.Math;

public class Exponential {
    public static int search(int[] inputArray, int target) {
        if(inputArray.length == 0){
            return -1;
        }
        if(inputArray[0] == target){
            return 0;
        }
        int index = 1;
        while(index < inputArray.length && inputArray[index] <= target){
            index *= 2;
        }
        return Binary.search(inputArray, target, index,Math.min(index, inputArray.length));
    }
}
