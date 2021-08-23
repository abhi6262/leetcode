# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        d = dict()
        if root:
            s =  deque([(0,root)])
            while s:
                i, n = s.popleft()
                d[i] = n.val
                if n.left:
                    s.append((2*i+1, n.left))
                if n.right:
                    s.append((2*i+2, n.right))
        return d    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root = None
        if data:
            s = []
            i, root = 0, TreeNode(data[0])
            del data[0]
            n = root
            while data:
                if 2*i+1 in data:
                    s.append((i,n))
                    n.left = TreeNode(data[2*i+1])
                    del data[2*i+1]
                    i, n = 2*i+1, n.left
                    continue
                if 2*i+2 in data:
                    s.append((i,n))
                    n.right = TreeNode(data[2*i+2])
                    del data[2*i+2]
                    i, n = 2*i+2, n.right
                    continue
                if s:
                    i, n = s.pop()
                    
                    
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
