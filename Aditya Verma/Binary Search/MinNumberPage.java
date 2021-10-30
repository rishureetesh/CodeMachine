class MinNumberPage{
    static boolean isEligibale(int[] Array, int max, int team){
        int sum = 0;
        int mates = 1;
        for(int array : Array){
            sum += array;
            if(sum > max){
                mates++;
                sum = array;
            }
            if(mates > max){
                return false;
            }
        }
        return true;
    }
    static int minNumberPage(int[] Array, int low, int high, int team){
        int result = -1;
        while(low <= high){
            int mid = (low +high)/2;
            if (isEligibale(Array, mid, team)){
                result = mid;
                high = mid-1;
            }else{
                low = mid+1;
            }
        }
        return result;
    }
    public static void main(String[] args){
        int[] Array = {10,20,30,40};
        int team = 2;
        int max = 40;
        //Find maximum value of the array if not sorted, else assign last element to max
        int sum = 100; //Sum of array
        int minNumber = minNumberPage(Array, max, sum, team);
        System.out.println(minNumber);
    }
}