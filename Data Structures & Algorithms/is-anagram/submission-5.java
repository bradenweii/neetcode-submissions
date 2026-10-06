class Solution {
    public boolean isAnagram(String s, String t) {
        int count=0;
        HashMap<Character,Integer> map1 = new HashMap<>();
        HashMap<Character,Integer> map2 = new HashMap<>();
        if(s.length()!=t.length()) return false;
        
        for(char c:s.toCharArray()){
            map1.put(c,map.getOrDefault(c,0)+1);
        }
        for(char c:t.toCharArray()){
            map2.put(c,map.getOrDefault(c,0)+1);
        }
        return map1.equals(map2);
    }
}
