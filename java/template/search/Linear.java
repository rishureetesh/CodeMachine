package java.template.search;

public class Linear{
    public int search(int[] inputArray, int target) {
        for(int index = 0; index < inputArray.length; index++){
            if(inputArray[index] == target){
                return index;
            }
        }
        return -1;
    }
    public int[] search(int[][] inputArray, int target) {
        for(int row = 0; row < inputArray.length; row++){
            for(int column = 0; column < inputArray.length; column++){
                if(inputArray[row][column] == target){
                    return new int[]{row,column};
                }
            }
        }
        return null;
    }
}
