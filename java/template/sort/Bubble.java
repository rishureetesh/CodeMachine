package java.template.sort;

public class Bubble {
    public int[] sort(int[] inputArray){
        for(int row=0;row < inputArray.length;row++){
            boolean updated = false;
            for(int column=1;column<inputArray.length - row;column++){
                if(inputArray[column-1] > inputArray[column]){
                    int temp = inputArray[column-1];
                    inputArray[column-1] = inputArray[column];
                    inputArray[column] = temp;
                    updated = true;
                }
            }
            if(!updated){
                break;
            }
        }
        return inputArray;
    }
}
