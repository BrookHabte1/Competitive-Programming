class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort(reverse=True)
        i=0
        j=1

        k=len(piles)
        total = 0
        while(j<k):
            total += piles[j]
            i+=1
            j=j+2
            k-=1
        return total
    