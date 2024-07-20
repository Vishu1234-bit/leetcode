class Solution:
    def canJump(self, nums: List[int]) -> bool:
        energy =0 
        for jumpEnergy in nums:
            if(energy<0):
                return False
            elif(jumpEnergy>energy):
                energy = jumpEnergy
            energy-=1
        return True
