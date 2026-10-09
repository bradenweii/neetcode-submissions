import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heapq.heappush(heap,-1*x)


        for _ in range(k-1):
            heapq.heappop(heap)
        return -1*heap[0]
        