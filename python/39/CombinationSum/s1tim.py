from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        self.combinationSumR(candidates, target, 0, [], ans)
        return ans
        
    def combinationSumR(self, candidates: List[int], target: int, idx: int, currentset: List[int], ans:List[int]) -> List[List[int]]:
        if target<=0:
            return
        elif target == candidates[idx]:
            ans.append([*currentset, target])
        else:
            for i in range(idx, len(candidates)):
                currentset.append(candidates[i])
                self.combinationSumR(candidates, target-candidates[i], i, currentset, ans)
                currentset.pop()


        

s=Solution()
input=[2,3,6,7]
target=18
ans=s.combinationSum(input, target)
print(ans)