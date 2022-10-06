class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        count = s.count(" ")
        if(count==len(s)):
            return (0)
        s=s.split()[-1]
        return len(s)
