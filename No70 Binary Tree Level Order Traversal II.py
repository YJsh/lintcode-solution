"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """

    def levelOrderBottom(self, root):
        # write your code here
        if not root:
            return []
        parents = [root]
        children = []
        vals = []
        while parents:
            data = []
            for node in parents:
                data.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            vals.insert(0, data)
            parents = children
            children = []
        return vals
