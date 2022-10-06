class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numsString = list(map(str,nums))
        output = ''
        for i in range(len(numsString)):
            for j in range(i,len(numsString)):
                if numsString[i] + numsString[j] > numsString[j] + numsString[i]:
                    continue
                else:
                    numsString[i],numsString[j] = numsString[j],numsString[i]
            output += numsString[i]
        return str(int(output))
        