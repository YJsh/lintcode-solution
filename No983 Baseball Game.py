class Solution:
    """
    @param ops: the list of operations
    @return:  the sum of the points you could get in all the rounds
    """
    def calPoints(self, ops):
        # Write your code here
        points = []
        for op in ops:
            if op == "C":
                points.pop()
            elif op == "D":
                points.append((points[-1] * 2))
            elif op == "+":
                points.append(points[-1] + points[-2])
            else:
                points.append(int(op))
        return sum(points)
