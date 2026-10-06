class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0:1}
        count = 0
        prefix = 0
        for n in nums:
            prefix+=n
            if prefix-k in map:
                count += map[prefix - k]
            map[prefix] = map.get(prefix, 0) + 1
        return count
        