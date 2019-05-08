# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = []
        queue = [root]
        if not root:
            return res
        while queue:
            temp = []
            for node in queue:
                if node:
                    res.append(node.val)
                    temp.append(node.left)
                    temp.append(node.right)
                else:
                    res.append('n')
            queue = temp
        return res

        # s = ""
        # queue = []
        # queue.append(root)
        # while queue:
        #     root = queue.pop(0)
        #     if root:
        #         s += str(root.val)
        #         queue.append(root.left)
        #         queue.append(root.right)
        #     else:
        #         s += "n"
        #     s += " "
        # return s

    def deserialize(self, data):

        tree = data
        # print(tree)
        # if tree[0] == "n":
        #     return None
        if not tree:
            return []
        queue = []
        root = TreeNode(int(tree[0]))
        queue.append(root)
        i = 1
        while queue:
            cur = queue.pop(0)
            if cur == None:
                continue
            cur.left = TreeNode(int(tree[i])) if tree[i] != "n" else None
            cur.right = TreeNode(int(tree[i + 1])) if tree[i + 1] != "n" else None
            i += 2
            queue.append(cur.left)
            queue.append(cur.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))