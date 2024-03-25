import warnings


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self, root_val: int):
        self.root = Node(val=root_val)

    def insert(self, val: int):
        curr = self.root

        while curr:
            if val < curr.val:
                # turn left
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(val=val)
                    break
            elif val > curr.val:
                # turn right
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val=val)
                    break
            else:
                # found an identical value
                warnings.warn(f'Node with value {val} already exists!')
                break

    def read(self) -> list:
        read_list = []
        if self.root:
            self.read_recursive(self.root, read_list)

        return read_list

    def read_recursive(self, root: Node, read_list: list):
        if root.left:
            self.read_recursive(root.left, read_list)

        read_list.append(root.val)

        if root.right:
            self.read_recursive(root.right, read_list)

    def delete(self, val: int):
        curr, prev = self.root, None
        target = None

        # find the target node
        while curr:
            if val < curr.val:
                # go left
                curr, prev = curr.left, curr
            elif val > curr.val:
                # go right
                curr, prev = curr.right, curr
            else:
                # found the node!
                target = curr
                break

        # if target is root node
        if target == self.root:
            if target.right and target.left:
                curr_min = target.right

                while curr_min.left:
                    curr_min = curr_min.left

                self.delete(curr_min.val)

                # set the target's val to curr_min value
                target.val = curr_min.val
                return
            elif target.left:
                self.root = target.left
                return
            elif target.right:
                self.root = target.right
                return
            else:
                # empty tree
                self.root = None
                return

        # if target is not found
        if not curr:
            raise Exception(f'Node with value {val} cannot be find in the tree!')

        # leaf node case
        if not target.left and not target.right:
            if prev.left == target:
                prev.left = None
                return
            else:
                prev.right = None
                return

        # One child to the left
        if not target.right:
            if prev.left == target:
                prev.left = target.left
                return
            else:
                prev.right = target.left
                return

        # One child to the right
        if not target.left:
            if prev.left == target:
                prev.left = target.right
                return
            else:
                prev.right = target.right
                return

        # Target has both children
        # find the smallest node on the right side of the target node
        curr_min = target.right

        while curr_min.left:
            curr_min = curr_min.left

        # re-delete with the new target being the that smallest curr_min val
        # in case that curr_min val has children
        self.delete(curr_min.val)

        # set the target's val to curr_min value
        target.val = curr_min.val


if __name__ == '__main__':
    bst = BST(10)
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    bst.insert(15)
    bst.insert(12)

    bst.delete(6)
