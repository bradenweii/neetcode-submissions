class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i=1;i<nums.length;i++){
            int x = 0;
            int n = target-nums[x];
            if(nums[i]==n){
                return new int[]{x,i};
            }else{
                x++;
            }
        }
        return new int[]{};
    }
}
