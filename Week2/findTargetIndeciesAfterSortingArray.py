class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        howMuch = []
        numbers = sorted(nums)
        for i in range(len(numbers)):
            if target == numbers[i]:
                howMuch.append(i)
        return(howMuch)
        