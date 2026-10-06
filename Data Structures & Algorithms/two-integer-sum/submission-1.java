class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = target-nums[0];
        for(int i=1;i<nums.length;i++){
            int x = 0;
            if(nums[i]==n){
                return new int[]{x,i};
            }else{
                n = target-nums[i];
                x=i;
            }
        }
        return new int[]{};
    }
}
