class Solution:
    def sortSentence(self, s: str) -> str:
        temp= s.split()
        word={}
        ans=''
        for i in temp:
            word[i[-1]]= i[:-1]
            print(word)
        print(sorted(word))
        for i in sorted(word):
            
            ans+=''.join(word[i])+' '
        ans=ans[:-1]
        return(ans)
        