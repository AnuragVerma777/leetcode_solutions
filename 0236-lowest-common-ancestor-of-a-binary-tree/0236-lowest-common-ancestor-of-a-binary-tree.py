class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        parent = {root: None}
        stack = [root]
        while p not in parent or q not in parent:   # stop once both are mapped
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()
        while p:                       # all ancestors of p, including p
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:      # climb from q until we meet one
            q = parent[q]
        return q