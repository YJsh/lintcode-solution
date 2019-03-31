class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """

    def __init__(self, v1, v2):
        # do intialization if necessary
        self.v = [v1, v2]
        self.index = 0

    """
    @return: An integer
    """

    def next(self):
        # write your code here
        v = self.v[self.index].pop(0)
        self.index = (self.index + 1) % 2
        return v

    """
    @return: True if has next
    """

    def hasNext(self):
        # write your code here
        if self.v[self.index]:
            return True
        self.index = (self.index + 1) % 2
        if self.v[self.index]:
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result
