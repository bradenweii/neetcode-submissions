class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        piles.sort()
        limit = int(h/n)

        return int(piles[-1]/limit)




