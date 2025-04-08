class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                pali=s[i:j]
                if pali==pali[::-1]:
                    count+=1
        return count
