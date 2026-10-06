class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = target-nums[0];
        for(int i=1;i<nums.length;i++){
            if(nums[i]==n){
                return new int[]{0,i};
            }
        }
        return new int[]{};
    }
}
