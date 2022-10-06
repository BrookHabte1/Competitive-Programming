class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i in range(len(l)):
                isArthemtic = True
                lists = sorted(nums[l[i]:r[i]+1])
                difference = lists[1] - lists [0]
                # print(difference)
                for j in range(len(lists)-1):
                        if lists[j+1] - lists[j] != difference:
                                isArthemtic = False             
                output.append(isArthemtic)
        return output
        