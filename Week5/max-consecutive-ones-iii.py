class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left=0
        for i in range(len(A)):
            if A[i]==0:
                k-=1
            if k<0:
                if A[left]==0:
                    k+=1
                left+=1
        return right-left+1
        