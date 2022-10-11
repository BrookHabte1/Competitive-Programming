class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = count.most_common(k)
        ans=[]
        for i in range(len(result)):
                ans.append(result[i][0])
        return ans
        