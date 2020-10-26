import unittest
from binTree import BinarySearchTree

class TestBst(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
    def testEmpty(self):
        self.assertIsNone(self.bst.root)

    def testInsert(self):
        self.bst.insert(10)
        self.bst.insert(6)
        self.bst.insert(15)
        self.bst.insert(3)
        self.bst.insert(8)
        self.bst.insert(20)
        
        self.bst.insert(13)

        self.assertEqual(self.bst.root.val, 10)

        self.assertEqual(self.bst.root.left.val, 6)
        self.assertEqual(self.bst.root.right.val, 15)

        self.assertEqual(self.bst.root.left.left.val, 3)
        self.assertEqual(self.bst.root.left.right.val, 8)
        
        self.assertEqual(self.bst.root.right.left.val, 13)
        self.assertEqual(self.bst.root.right.right.val, 20)

        self.assertIsNone(self.bst.root.left.left.left)
        self.assertIsNone(self.bst.root.left.left.right)
        
        self.assertIsNone(self.bst.root.left.right.left)
        self.assertIsNone(self.bst.root.left.right.right)
        
        self.assertIsNone(self.bst.root.right.right.right)
        self.assertIsNone(self.bst.root.right.right.left)
        
        self.assertIsNone(self.bst.root.right.left.left)
        self.assertIsNone(self.bst.root.right.left.left)

    def testInsertRec(self):
        self.bst.insertRec(10)
        self.bst.insertRec(6)
        self.bst.insertRec(15)
        self.bst.insertRec(3)
        self.bst.insertRec(8)
        self.bst.insertRec(20)
        self.bst.insertRec(13)

        self.assertEqual(self.bst.root.val, 10)

        self.assertEqual(self.bst.root.left.val, 6)
        self.assertEqual(self.bst.root.right.val, 15)

        self.assertEqual(self.bst.root.left.left.val, 3)
        self.assertEqual(self.bst.root.left.right.val, 8)
        
        self.assertEqual(self.bst.root.right.left.val, 13)
        self.assertEqual(self.bst.root.right.right.val, 20)

        self.assertIsNone(self.bst.root.left.left.left)
        self.assertIsNone(self.bst.root.left.left.right)
        
        self.assertIsNone(self.bst.root.left.right.left)
        self.assertIsNone(self.bst.root.left.right.right)
        
        self.assertIsNone(self.bst.root.right.right.right)
        self.assertIsNone(self.bst.root.right.right.left)
        
        self.assertIsNone(self.bst.root.right.left.left)
        self.assertIsNone(self.bst.root.right.left.left)


if __name__ == "__main__":
    unittest.main()