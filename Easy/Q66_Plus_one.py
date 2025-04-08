class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=int("".join(list(map(str,digits))))
        num+=1

        l=[]
        for i in str(num):
            l.append(int(i))
        return l
