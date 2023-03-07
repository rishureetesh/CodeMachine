import java.util.*;
class CountAnagramOccurance{
    static int checkFreq(int freq){
        if(freq > 0){
            return freq-1;
        }else{
            return Integer.MAX_VALUE-1;
        }
    }
    static int increaseFreq(int freq){
        return (freq+1)%Integer.MAX_VALUE;
    }
    public static void main(String [] args){
        String data = "ofrforofro";
        String pattern = "for";
        int count = pattern.length();
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for(int i =0; i < pattern.length();i++){
            char ch = pattern.charAt(i);
            if(map.containsKey(ch)){
                map.put(ch, map.get(ch) +1);
            }else{
                map.put(ch, Integer.valueOf(1));
            }
        }
        for(int j=0, i=0;j<data.length();j++){
            char ch = data.charAt(j);
            if(map.containsKey(ch)){
                int freq = map.get(ch);
                if(freq > 0){
                    count--;
                }
                map.put(ch, checkFreq(freq));
            }
            if (j-i+1 == pattern.length()){
                if (count == 0){
                    System.out.println("Found at index : "+i+"->"+j);
                }
                if(map.containsKey(data.charAt(i))){
                    map.put(data.charAt(i), increaseFreq(map.get(data.charAt(i))));
                    if(map.get(data.charAt(i)) != 0 && map.get(data.charAt(i)) < pattern.length())
                        count++;
                }
                i++;
            }
        }
    }
}