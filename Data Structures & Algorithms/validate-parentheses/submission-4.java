class Solution {
    public boolean isValid(String s) {
      Stack<Character> stack = new Stack<>();
        
        // Iterate through each character in the string
        for (char c : s.toCharArray()) {
            // Push opening brackets onto the stack
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            }
            // Handle closing brackets
            else {
                // If stack is empty, there's no matching opening bracket
                if (stack.isEmpty()) {
                    return false;
                }
                
                char top = stack.pop();
                // Check if the popped opening bracket matches the current closing bracket
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        
        // If the stack is empty, all brackets are matched; otherwise, it's invalid
        return stack.isEmpty();

    }
}
