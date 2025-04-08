class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(len(s)-1):
            count=count+(abs(ord(s[i])-ord(s[i+1])))
        return count
