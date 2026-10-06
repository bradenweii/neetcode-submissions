class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set  = new HashSet<>();
        for(int n:nums){
            set.add(n);
        }
        int count = 0;
        for(int n:set){
            if(!set.contains(n-1)){
                int length =1;
                while(set.contains(n+length)){
                    length++;
                }
                count = Math.max(length,count);
            }
        }
        return count;
    }
}
