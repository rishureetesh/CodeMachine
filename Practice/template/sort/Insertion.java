package Practice.template.sort;

public class Insertion {
    public int[] sort(int[] inputArray){
        for(int row=2;row < inputArray.length;row++){
            int min = inputArray[row];
            int column = row - 1;
            while(column > 0 && inputArray[column] > min){
                inputArray[column+1] = inputArray[column];
                column--;
            }
            inputArray[column] = min;
        }
        return inputArray;
    }
}
