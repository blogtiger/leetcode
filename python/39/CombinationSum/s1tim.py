from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=self.combinationSum(candidates, target, 0)
        return ans
        
    def combinationSum(self, candidates: List[int], target: int, idx: int, currentset: List[int]) -> List[List[int]]:
        if target == candidates[idx]:
            return [*currentset, target]
        

s=Solution()
input=[2,3,6,7]
target=4
ans=s.combinationSum(input, target)
print(ans)
print(input)

print(target)
