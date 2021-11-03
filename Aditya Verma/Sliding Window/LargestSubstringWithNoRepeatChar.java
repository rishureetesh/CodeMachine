import java.util.HashMap;
import java.util.Map;

class LargestSubstringWithNoRepeatChar{
    public static void main(String[] args) {
        Map<Character,Integer> map = new HashMap<Character,Integer>();
        String data = "abaaabgdasas";
        int start=0,end=0;
        for(int i=0,j=0; j<data.length(); j++) {
            char ch = data.charAt(j);
            while(map.containsKey(ch) && i <= j){
                map.remove(data.charAt(i++));
            }
            map.put(ch,1);
            if(j-i+1 >= end-start+1){
                start=i;
                end=j;
            }
        }
        System.out.println(start + "------------" + end+"Count -> "+(end-start+1));
    }
}