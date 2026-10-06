class Solution {
    public boolean isAnagram(String s, String t) {
        int count=0;
        if(s.length()!=t.length()) return false;
        for(int i=0;i<s.length();i++){
            count+= s.charAt(i)-t.charAt(i);
        }
        return count==0;
    }
}
