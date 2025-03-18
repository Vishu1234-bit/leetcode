class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        gcd = math.gcd(targetX,targetY)
        return gcd&(gcd-1) == 0
