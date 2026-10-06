class Solution {
    public boolean isValid(String s) {
       Stack<Character> stack = new Stack<>(); 
       for(int i=0;i<s.length()/2;i++){
        stack.push(s.charAt(i));
       }

       for(int i=s.length()/2;i<s.length();i++){
        if(stack.isEmpty()) return false;
        if(s.charAt(i)==')'&&stack.pop()!='('){
            return false;
        }else if(s.charAt(i)=='}'&&stack.pop()!='{'){
            return false;
        }
        else if(s.charAt(i)==']'&&stack.pop()!='['){
            return false;
        }
       }
       
       return true;

    }
}
