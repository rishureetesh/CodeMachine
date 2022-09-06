import java.util.*;
class SearchTwoDArray{
    static ArrayList<Integer> result = new ArrayList<Integer>();
    static ArrayList<Integer> searchTwoDArray(int[][] Array, int low, int high, int Element){
        if(low == Array.length || high < 0){
            result.add(-1);
            return result;
        }else if(Array[low][high] == Element){
            result.add(low);
            result.add(high);
            return result;
        }else if(Array[low][high] > Element){
            high--;
        }else{
            low++;
        }
        return searchTwoDArray(Array, low, high, Element);
    }
    public static void main(String[] args) {
        int[][] Array = {
            {1,12,21,31,41},
            {4,13,25,33,42},
            {7,17,27,35,47},
            {10,19,29,37,49}
        };
        ArrayList arrayIndex = searchTwoDArray(Array, 0, Array[0].length-1, 11);
        System.out.println(arrayIndex);
    }
}