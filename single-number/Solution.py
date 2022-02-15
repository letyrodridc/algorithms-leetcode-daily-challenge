class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = dict()
        
        for x in nums:
            if x in c.keys():
                c[x] += 1
            else:
                c[x] = 1
                
        return [k for k, v in  c.items() if v == 1][0]