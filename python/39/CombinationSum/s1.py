from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #Results list
        ans = []
        #Possible combinations
        tmp = []

        def helper(idx, total):
            """Trace back to find the sum of combinations
            Args:
                IDX: select element index
                Total: elements and in composition
            """
            #Base conditions
            #When the sum of the elements is greater than the target value, it is returned directly
            if total > target:
                return
            #When the sum of the elements is equal to the target value, the combination is added to the result and returned
            if total == target:
                ans.append(tmp[::])
                return
            
            #Enter branches and avoid repeated combinations
            for i in range(idx, len(candidates)):
                #Update the total value,
                total += candidates[i]
                #Also attempts to add the current element to the composition
                tmp.append(candidates[i])
                #Recursion again
                #Here you can see the article legend, recursion down, the optional elements are selected from themselves
                #At the same time, composition duplication can be avoided because the corresponding elements in front of index I will not be selected again
                helper(i, total)
                #Backtracking, backtracking, combining elements and total values
                tmp.pop()
                total -= candidates[i]
            
        total = 0
        helper(0, total)
        return ans
        

s=Solution()
ans=s.combinationSum([2,3,6,7], 7)
print(ans)