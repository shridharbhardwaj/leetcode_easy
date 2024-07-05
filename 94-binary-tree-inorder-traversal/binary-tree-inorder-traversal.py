# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._inorderTraversalHelper(root, result)
        return result
    
    def _inorderTraversalHelper(self, root: Optional[TreeNode], result: List[int]):
        if root is not None:
            self._inorderTraversalHelper(root.left, result)
            result.append(root.val)
            self._inorderTraversalHelper(root.right, result)