class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_length=len(needle)
        if needle_length>len(haystack):
            return -1
        for i in range(len(haystack)-needle_length+1):
            if haystack[i:i+needle_length]==needle:
                return i
        return -1
        
