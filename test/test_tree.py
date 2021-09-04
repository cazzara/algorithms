import unittest
import pytest


from src.tree import BinarySearchTree


class TestBinarySearchTreeInsert(unittest.TestCase):
    def setUp(self):
        self.t = BinarySearchTree()

    def test_BinarySearchTree_init(self):
        assert isinstance(self.t, BinarySearchTree)

    def test_BinarySearchTree_insert(self):
        self.assertEquals(self.t.height, -1) # empty tree has height -1
        self.t.insert(8)
        self.assertEquals(self.t.height, 0) # tree with only one node has height 0
        self.assertEquals(self.t.root.value, 8)
        for i in [3,10,1,6,4,7,14,13]:
            self.t.insert(i)
        self.assertEquals(self.t.height, 3)

