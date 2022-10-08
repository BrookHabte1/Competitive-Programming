class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        maxNums=0
        while (j>i):
                maxNums=max(maxNums,nums[i]+nums[j])
                i += 1
                j -= 1
        return (maxNums)
        