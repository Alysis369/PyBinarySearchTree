from typing import Any


class Node:
    def __init__(self, val: int = None, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self, root_value: int):
        self.root = Node(val=root_value)

    def insert(self, val: Any):
        curr = self.root

        while True:
            if val < curr.val:
                if curr.left:
                    # move to left node
                    curr = curr.left
                else:
                    # place new node here
                    curr.left = Node(val=val)
                    break

            else:
                if curr.right:
                    # move to the right node
                    curr = curr.right
                else:
                    # place new node here
                    curr.right = Node(val=val)
                    break

    def delete(self, val: int):
        # find the node
        target = self.find(val)

        # TODO: EC for right does not exist
        curr, prev = target.right, None

        # find smallest node
        while curr.left:
            curr, prev = curr.left, curr

        # change the target node value
        target.val = curr.val
        prev.left = curr.right

    def find(self, val: int) -> Node:
        curr = self.root

        while curr:
            if val < curr.val:
                curr = curr.left  # go left
            elif val > curr.val:
                curr = curr.right  # go right
            else:
                # found the node
                return curr

        raise KeyError('Value not found in BST.')

    def bfs_traverse(self):
        # use queue method
        q = [self.root]
        traverse_list = []
        while q:
            curr = q.pop(0)

            if curr:  # ignore empty ends
                traverse_list.append(curr.val)

                # put children to q
                q.append(curr.left)
                q.append(curr.right)

        return traverse_list

    def dfs_traverse(self):
        traverse_list = []

        self.dfs_recursive(self.root, traverse_list)

        return traverse_list

    def dfs_recursive(self, root: Node, traverse_list: list):
        if root:
            self.dfs_recursive(root.left, traverse_list)
            traverse_list.append(root.val)
            self.dfs_recursive(root.right, traverse_list)
