package search;
import java.lang.Math;

public class Jump {
    public int search(int[] inputArray, int target) {
        int inputLength = inputArray.length;
        int step = (int)Math.sqrt(inputLength);
        int prevStep = 0;
        while(inputArray[Math.min(step, inputLength)-1] < target){
            prevStep = step;
            step += (int)Math.sqrt(inputLength);
            if(prevStep >= inputLength){
                return -1;
            }
        }
        while(inputArray[prevStep] < target){
            prevStep += 1;
            if(prevStep == Math.min(step, inputLength)){
                return -1;
            }
        }
        if(inputArray[prevStep] == target){
            return prevStep;
        }
        return -1;
    }
}
