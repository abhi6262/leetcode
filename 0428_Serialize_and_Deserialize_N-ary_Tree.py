"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return None
        q = deque([root, None])
        a = []
        while q:
            l = len(q)
            for i in range(l):
                n = q.popleft()
                if n:
                    a.append(str(n.val))
                    for c in n.children:
                        q.append(c)
                    q.append(None)
                else:
                    a.append('#')
        s = ','.join(a)
        return s
