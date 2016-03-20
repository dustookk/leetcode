class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        lst = [0] * (num + 1)
        milestone = 0
        nextMilestone = 2
        for i in range(1, num + 1):
            if i is nextMilestone:
                milestone = nextMilestone 
                nextMilestone = nextMilestone * 2
            
            lst[i] = lst[i - milestone] + 1
        return lst


    def isMilestone(self, num):
        return  num & num -1 == 0 

