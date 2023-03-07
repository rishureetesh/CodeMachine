import java.util.HashMap;
import java.util.Map;

class LongestSubStringWithKDistinctChar {
    public static void main(String[] args) {
        String data = "abasdsdsdsdsd";
        int kDistinct = 3;
        int start = -1, end = -1;
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for(int i=0,j=0; j<data.length(); j++) {
            char ch = data.charAt(j);
            if(map.containsKey(ch)){
                map.put(ch, map.get(ch)+1);
            }else{
                map.put(ch, 1);
            }
            while(map.size() > kDistinct && i<j){
                if(map.get(data.charAt(i)) > 1) {
                    map.put(data.charAt(i),map.get(data.charAt(i))-1);
                }else{
                    map.remove(data.charAt(i));
                }
                i++;
            }
            if(map.size() == kDistinct && (end-start+1 < j-i+1)){
                start = i;
                end = j;
            }
        }
        System.out.println(start + "------------" + end+"Count -> "+(end-start+1));
    }    
}
