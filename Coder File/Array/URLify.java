public class URLify{
    public static void main(String[] args){
        // char[] ch = " Mr. John Smith   ".toCharArray();
        char[] ch = "                 ".toCharArray();
        int initialIndex = 0;
        int lastIndex = ch.length-1;

        while(initialIndex<ch.length && ch[initialIndex] == ' '){
            initialIndex++;
        }

        while(ch[lastIndex] == ' '){
            if(lastIndex > 0 && initialIndex > lastIndex){
                System.out.println("String only contains spaces!!");
                return;
            }
            lastIndex--;
        }

        StringBuffer sb = new StringBuffer();
        for(;initialIndex <= lastIndex; initialIndex++){
            if(ch[initialIndex] == ' '){
                sb.append("%20");
            }else{
                sb.append(ch[initialIndex]);
            }
        }
        System.out.println("New String is : " + sb.toString());
    }
}