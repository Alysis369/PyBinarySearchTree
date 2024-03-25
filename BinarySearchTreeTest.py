import unittest
from BinarySearchTree import BST
from random import randint, shuffle


class BSTTestCase(unittest.TestCase):
    def test_insert(self):
        bst = BST(10)
        bst.insert(5)
        bst.insert(7)

        self.assertEqual(5, bst.root.left.val)
        self.assertEqual(7, bst.root.left.right.val)

    def test_read(self):
        bst = BST(10)
        bst.insert(5)
        bst.insert(7)
        bst.insert(6)
        bst.insert(15)
        bst.insert(12)

        self.assertEqual([5, 6, 7, 10, 12, 15], bst.read())

    def test_delete(self):
        bst = BST(10)
        bst.insert(5)
        bst.insert(7)
        bst.insert(6)
        bst.insert(15)
        bst.insert(12)

        bst.delete(6)
        bst.delete(12)
        self.assertEqual([5, 7, 10, 15], bst.read())

    def test_massive_n(self):
        bst = BST(50)
        for _ in range(10):
            bst.insert(randint(1, 101))

        existing = bst.read()
        shuffle(existing)
        print(existing)

        for _ in range(len(existing)):
            print(existing)
            element = existing.pop()

            print(bst.root.val)
            bst.delete(element)
            self.assertEqual(sorted(existing), bst.read())


if __name__ == '__main__':
    unittest.main()
