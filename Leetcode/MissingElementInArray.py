# public class MissingElementInArray {
#     public static void main(String[] args) {
#         int[] inputArray = new int[]{1,2,3,4,5,5,7,7,9};
#         int total = inputArray.length;
#         int index = 0;
#         while(index<total){
#             if(inputArray[inputArray[index]-1] != inputArray[index]){
#                 int temp = inputArray[index];
#                 inputArray[index] = inputArray[temp-1];
#                 inputArray[temp-1] = temp;
#             }else{
#                 index++;
#             }
#         }
#         for(int row=0;row<total;row++){
#             if(inputArray[row]-1 != row){
#                 System.out.println("Missing Element : "+(row+1)+", Duplicate : "+inputArray[row]);
#             }
#         }
#     }
# }
