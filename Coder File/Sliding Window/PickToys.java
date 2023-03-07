import java.util.HashMap;
import java.util.Map;

public class PickToys {
    public static void main(String[] args) {
        String data = "aabaaabcccccbbsa";
        int maxToys = 2;
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        int start=0,end=0;
        for(int i =0,j=0; j< data.length();j++){
            char ch = data.charAt(j);
            if(map.containsKey(ch)){
                map.put(ch,map.get(ch)+1);
            }else{
                map.put(ch,1);
            }
            while(map.size()>maxToys){
                if(map.containsKey(data.charAt(i)) && map.get(data.charAt(i)) > 1){
                    map.put(data.charAt(i),map.get(data.charAt(i))-1);
                }else{
                    map.remove(data.charAt(i));
                }
                i++;
            }
            if(map.size() == maxToys && j-i+1 > end-start+1){
                start=i;
                end=j;
            }
        }
        System.out.println(start+"------------"+end+" Size of subarray : "+(end-start+1));
    }
}
