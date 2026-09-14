class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # node found
            
            # case 1: no left child
            if not root.left:
                return root.right

            # case 2: no right child
            if not root.right:
                return root.left

            # case 3: two children
            temp = root.right
            while temp.left:
                temp = temp.left

            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        return root