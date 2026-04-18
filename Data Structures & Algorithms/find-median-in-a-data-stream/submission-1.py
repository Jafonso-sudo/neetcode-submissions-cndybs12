# Solution
# - Keep a max-heap w/ half the smallestelements & a min-heap w/ half the largest elements
# - When adding a new number check where it fits and shift the top accordingly

class MedianFinder:

    def __init__(self):
        self.first_half = []
        self.second_half = []
        

    def addNum(self, num: int) -> None:
        # Code can be made a bit nicer (notice how the final line inside the nested if is the same for both, can simplify a bit if I cared enough)
        if len(self.second_half) < len(self.first_half):
            if num > self.first_half[0]:
                heapq.heappush(self.second_half, num)
            else:
                max_first = heapq.heappushpop_max(self.first_half, num)
                heapq.heappush(self.second_half, max_first)
        else:
            if not self.second_half or num < self.second_half[0]:
                heapq.heappush_max(self.first_half, num)
            else:
                min_second = heapq.heappushpop(self.second_half, num)
                heapq.heappush_max(self.first_half, min_second)

    def findMedian(self) -> float:
        if (len(self.first_half) + len(self.second_half)) % 2 == 0:
            return (self.first_half[0] + self.second_half[0]) / 2
        else:
            return self.first_half[0]
        
        