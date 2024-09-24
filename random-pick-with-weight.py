import random
class Solution:

    def __init__(self, w: List[int]):
        self.w=w

    def pickIndex(self) -> int:
        indices = range(len(self.w))
        total_sum =sum(self.w)
        probabilities=[]
        for i in self.w:
            probabilities.append(i/total_sum)
        index = random.choices(indices,probabilities,k=1)
        return index[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
