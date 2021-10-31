class FirstNegetiveInWindow{
    public static void main(String[] args){
        int[] Array = {1,-2,-3,4,-5,6,-7,-8,9,10,11,12};
        int window = 3;
        int[] negetiveArray = new int[Array.length-window];
        int start = 0, end = 0;
        for (int i = 0,j = 0; j < Array.length;j++){
            if (Array[j] < 0){
                negetiveArray[end++] = Array[j];
            }
            if(i+j+1 >= window){
                if(negetiveArray[start] < 0)
                    System.out.println(negetiveArray[start]);
                if(Array[i++] == negetiveArray[start]){
                    start++;
                }
            }
        }
    }
}