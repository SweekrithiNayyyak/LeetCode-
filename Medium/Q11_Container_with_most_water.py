class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        maximum=0
        while j>i:
            product=min(height[i],height[j])*(j-i)
            maximum=product if product>maximum else maximum
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return maximum
