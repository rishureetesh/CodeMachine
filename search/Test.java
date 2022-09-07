package search;
//Find the missing and duplicate element in a array
public class Test {
    public static void main(String[] args) {
        int[] inputArray = new int[]{1,2,3,4,5,5,7,8,9};
        int pos = Interpolation.search(inputArray, 5);
        System.out.println(pos);
    }
}
