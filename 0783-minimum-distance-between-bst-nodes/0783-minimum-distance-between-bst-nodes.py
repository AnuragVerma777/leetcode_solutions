class Solution(object):
    def minDiffInBST(self, root):
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)       # 1. go left
            values.append(node.val)  # 2. visit node
            inorder(node.right)      # 3. go right

        inorder(root)                # values is now sorted

        ans = float('inf')
        for i in range(1, len(values)):
            ans = min(ans, values[i] - values[i - 1])
        return ans 
        