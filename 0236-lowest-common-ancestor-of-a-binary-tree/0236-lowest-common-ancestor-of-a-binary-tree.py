class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # Base case: empty tree, or we hit p or q
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q found on different sides, so this node is the LCA
        if left and right:
            return root

        # Otherwise return whichever side found something (or None)
        return left if left else right
       