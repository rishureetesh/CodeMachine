public class StringCompression {
    public static void main(String[] args) {
        String string = "aabcccccaaa";
        char ch = string.charAt(0);
        int count = 1;
        StringBuffer sb = new StringBuffer();
        sb.append(ch);
        for(int index = 1; index < string.length(); index++){
            if(string.charAt(index) == ch){
                count++;
                continue;
            }else{
                sb.append(count);
                ch = string.charAt(index);
                sb.append(ch);
                count = 1;
            }
        }
        sb.append(count);
        System.out.println(sb.toString());
    }
}`  
