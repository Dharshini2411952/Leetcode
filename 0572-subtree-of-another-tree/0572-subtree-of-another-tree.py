class Solution:
    def isSubtree(self,root,subroot):
        if not subroot:
            return True
        if not root:
            return False
        if self.isSame(root,subroot):
            return True
        return(self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot))
    def isSame(self,a,b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return (self.isSame(a.left,b.left)and self.isSame(a.right,b.right))