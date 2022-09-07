package sort;

public class Quick {
    public void sort(int[] inputArray){
        quickSort(inputArray, 0, inputArray.length-1);
    }

    public void quickSort(int[] inputArray, int left, int right){
        if(left < right){
            int partition = partition(inputArray, left, right);
            quickSort(inputArray, left, partition-1);
            quickSort(inputArray, partition+1, right);
        }
    }

    public void swap(int[] inputArray, int initial, int target){
        int temp = inputArray[initial];
        inputArray[initial] = inputArray[target];
        inputArray[target] = temp;
    }

    public int partition(int[] inputArray, int left, int right){
        int pivot = inputArray[right];
        int primeIndex=left-1;
        for(int secondIndex=left; secondIndex<=right-1;secondIndex++){
            if(inputArray[secondIndex]<= pivot){
                primeIndex += 1;
                swap(inputArray, primeIndex, secondIndex);
            }
        }
        swap(inputArray, primeIndex+1, right);
        return primeIndex;
    }
}