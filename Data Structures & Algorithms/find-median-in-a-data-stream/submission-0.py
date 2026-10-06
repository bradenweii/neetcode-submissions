class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        self.data.append(num)
        

    def findMedian(self) -> float:
        sum = 0
        for n in self.data:
            sum+=n
        return float(sum)/len(self.data)
        
        