class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        if(nums.length==1) return 1;
        int count = 0;
        for(int i=1;i<nums.length;i++){
            if(nums[i]-nums[i-1]==1 || nums[i]-nums[i-1]==0 || nums[i]-nums[i-1]==-1){
                count++;
            }
        }
        System.out.println(nums);
        return count;
    }
}
