class OnceAppearingElement{
    static int onceAppearingElement(int[] Array, int low, int high){
        if(low > high){
            return -1;
        }
        int mid = low + (high - low) / 2;
        int prev = (mid + Array.length - 1) % Array.length;
        int next = (mid + 1) % Array.length;
        if (Array[mid] != Array[prev] && Array[mid] != Array[next])
            return Array[mid];
        else if ((Array[mid] == Array[next] && mid % 2 == 0) || (Array[mid] == Array[prev] && mid % 2 != 0))
            return onceAppearingElement(Array, mid+1, high);
        else
            return onceAppearingElement(Array, low, mid-1);
    }
    public static void main(String[] args){
        int[] Array = {1,1,2,2,3,3,4,4,5};
        int data = onceAppearingElement(Array, 0, Array.length-1);
        System.out.println(data);
    }
}