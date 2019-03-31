class Solution:
    """
    @param n: a number represent year
    @return: whether year n is a leap year.
    """
    def isLeapYear(self, n):
        # write your code here
        if n % 4:
            return False
        if n % 100 == 0:
            return n % 400 == 0
        return True
