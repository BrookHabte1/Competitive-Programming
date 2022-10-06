class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        for i in range(len(nums)):
            index = i
            for j in range(len(nums)):
                if nums[j] < nums [i]:
                    output[index] += 1
            index += 1
        return(output) 
        