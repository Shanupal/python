class Solution(object):
    def maxSubArray(self, nums :list[int]) -> int:
        maxsub nums[0]
        cursum=0

        for n in nums:
            if cursum <0:
                cursum =0
                cursum += 0
                cursum +=n
                maxsub = max(maxsab, cursum)
                return maxsub
       