"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None
        r = TreeNode(root.val)
        s1 = [root]
        s2 = [r]
        while s1:
            n1 = s1.pop()
            n2 = s2.pop()
            l = len(n1.children)
            n2.left = TreeNode(l)
            c = n2.left
            for i in range(l):
                c.right = TreeNode(n1.children[i].val)
                c = c.right
                s1.append(n1.children[i])
                s2.append(c)
        return r
        
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None
        s1 = [data]
        r = Node(data.val, [])
        s2 = [r]
        while s1:
            n1 = s1.pop()
            n2 = s2.pop()
            c = n1.left
            l = c.val
            for i in range(l):
                c = c.right
                n = Node(c.val, [])
                n2.children.append(n)
                s1.append(c)
                s2.append(n)
        return r
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
