class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest=0
        left=0
        sett=set()
        n=len(s)
        for right in range(n):
            while s[right] in sett:
                sett.remove(s[left])
                left+=1
                
            longest=max(longest,(right-left)+1)
            sett.add(s[right])
        return longest
