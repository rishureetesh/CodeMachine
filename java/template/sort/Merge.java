package java.template.sort;
import java.lang.Math;

public class Merge {
    public void sort(int[] inputArray){
        mergeSort(inputArray, 0, inputArray.length - 1);
    }

    public void mergeSort(int[] inputArray, int left, int right){
        if(left < right){
            int mid = (int)Math.floor(left + (right - left)/2);
            mergeSort(inputArray, left, mid);
            mergeSort(inputArray, mid+1, right);
            merge(inputArray, left, mid, right);
        }
    }

    public void merge(int[] inputArray, int left, int middle, int right){
        int lengthOne = middle-left+1;
        int lengthTwo = right-middle;

        int inputArrayOne[] = new int[lengthOne];
        int inputArrayTwo[] = new int[lengthTwo];

        for(int index=1; index<lengthOne;index++){
            inputArrayOne[index] = inputArray[left+index];
        }

        for(int index=1; index<lengthTwo;index++){
            inputArrayTwo[index] = inputArray[middle+index];
        }

        int indexOne=0;
        int indexTwo = 0;
        int index =left;
        while(indexOne < lengthOne && indexTwo < lengthTwo){
            if(inputArrayOne[indexOne] <  inputArrayTwo[indexTwo]){
                inputArray[index++] = inputArrayOne[indexOne++];
            }else{
                inputArray[index++] = inputArrayTwo[indexTwo++];
            }
        }
        while(indexOne < lengthOne){
            inputArray[index++] = inputArrayOne[indexOne++];
        }
        while(indexTwo < lengthTwo){
            inputArray[index++] = inputArrayTwo[indexTwo++];
        }
    }
}
