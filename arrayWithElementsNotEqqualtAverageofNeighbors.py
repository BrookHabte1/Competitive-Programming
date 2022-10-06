class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        numsSorted = sorted(nums)
        a = collections.deque(numsSorted)
        output = []
        while len(a)>0:
            if len(a)>0:
                output.append(a.popleft())
            if len(a)>0:
                output.append(a.pop())
        return output
        