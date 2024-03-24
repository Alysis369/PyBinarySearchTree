import unittest
from BinarySearchTree import BST


class BSTTestCase(unittest.TestCase):
    def testInsert(self):
        bst = BST(10)
        bst.insert(2)
        bst.insert(12)
        bst.insert(4)
        bst.insert(3)
        bst.insert(5)

        self.assertEqual(10, bst.root.val)
        self.assertEqual(2, bst.root.left.val)
        self.assertEqual(12, bst.root.right.val)
        self.assertEqual(4, bst.root.left.right.val)
        self.assertEqual(3, bst.root.left.right.left.val)

    def testBfsTraverse(self):
        bst = BST(10)
        bst.insert(2)
        bst.insert(12)
        bst.insert(4)
        bst.insert(3)
        bst.insert(5)

        self.assertEqual([10, 2, 12, 4, 3, 5], bst.bfs_traverse())

    def testFind(self):
        bst = BST(10)
        bst.insert(2)
        bst.insert(12)
        bst.insert(4)
        bst.insert(3)
        bst.insert(5)

        node = bst.find(4)
        self.assertEqual(3, node.left.val)
        self.assertEqual(5, node.right.val)

    def testDelete(self):
        bst = BST(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(12)
        bst.insert(13)
        bst.delete(10)



if __name__ == '__main__':
    unittest.main()
