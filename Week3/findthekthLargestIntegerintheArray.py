class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        numsSorted = list(map(int,nums))
        numsSorted.sort(reverse=True)
        numsSortedStr = list(map(str,numsSorted))
        return numsSortedStr[k-1]
        