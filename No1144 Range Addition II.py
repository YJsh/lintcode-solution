class Solution:
    """
    @param m: an integer
    @param n: an integer
    @param ops: List[List[int]]
    @return: return an integer
    """
    def maxCount(self, m, n, ops):
        # write your code here
        minM = m
        minN = n
        for opM, opN in ops:
            if not minM or minM > opM:
                minM = opM
            if not minN or minN > opN:
                minN = opN
        return minM * minN
