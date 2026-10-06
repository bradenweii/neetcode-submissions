class Solution {
    public boolean isPalindrome(String s) {
        String str = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        System.out.println(str);
        for(int i=0;i<str.length()/2;i++){
            if(str.charAt(i)!=str.charAt(s.length()-i-1)){
                return false;
            }
        }
        
        return true;
    }
}
