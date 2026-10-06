class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0

        for j in range(1,len(nums)):
            first = nums[i]
            if target - first == nums[j]:
                return [i,j]
            
        return []