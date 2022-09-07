package sort;

public class Heap {
    public void sort(int[] inputArray){

        int N = inputArray.length;
 
        for (int i = N / 2 - 1; i >= 0; i--)
            heapify(inputArray, N, i);
 
        for (int index = N - 1; index > 0; index--) {
            int temp = inputArray[0];
            inputArray[0] = inputArray[index];
            inputArray[index] = temp;
 
            heapify(inputArray, index, 0);
        }
    }

    void heapify(int inputArray[], int N, int index)
    {
        int largest = index;
        int left = 2 * index + 1;
        int right = 2 * index + 2;
 
        if (left < N && inputArray[left] > inputArray[largest])
            largest = left;
 
        if (right < N && inputArray[right] > inputArray[largest])
            largest = right;
 
        if (largest != index) {
            int swap = inputArray[index];
            inputArray[index] = inputArray[largest];
            inputArray[largest] = swap;
 
            heapify(inputArray, N, largest);
        }
    }
}
