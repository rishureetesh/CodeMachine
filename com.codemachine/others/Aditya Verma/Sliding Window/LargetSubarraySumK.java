class LargetSubarraySumK{
    public static void main(String [] args){
        int[] Array = {9,2,1,4,6,2,4,3,-1,0,2};
        int sumWindow = 12;
        int start,end,sum;
        start = end = sum = 0;
        for(int i=0,j=0;j<Array.length;j++){
            sum+=Array[j];
            while(sum > sumWindow){
                sum -= Array[i++];
            }
            if(sum == sumWindow && end-start+1 <= j-i+1){
                start = i;
                end = j;
            }
        }
        System.out.println(start+"------------"+end+" Size of subarray : "+(end-start+1));
    }
}