class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s)==1 :
            return True
        start,end=0,len(s)-1
        print(s[19], s[81])

        extra_char=False
        while start<=end:
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                print(s[start],s[end])
                if extra_char == True:
                    return False
                extra_char = True
                if s[start+1]!=s[end]:
                    end-=1
                else:
                    start+=1
        return True

ans=Solution().validPalindrome('aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga')
print(ans)