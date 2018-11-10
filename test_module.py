import unittest
import main


class TestList(unittest.TestCase):
    def test_append(self):
        dy = main.DynArray()
        self.assertEqual(dy.capasity, 16)
        for i in range(16):
            dy.append(i)
            self.assertEqual(dy[i], i)

    def test_append2(self):
        dy = main.DynArray()
        self.assertEqual(dy.capasity, 16)
        for i in range(100):
            dy.append(i)
            self.assertEqual(dy[i], i)
        self.assertGreater(dy.capasity, 100)

    def test_insert(self):
        dy = main.DynArray()
        dy.append(1)
        dy.append(1)
        dy.append(1)
        dy.insert(10, 3)
        for i in range(len(dy)):
            self.assertNotEqual(dy[i], 3)
            self.assertEqual(dy[i], 1)

    def test_delete(self):
        dy = main.DynArray()
        dy.append(1)
        dy.append(1)
        dy.append(1)
        dy.append(1)
        self.assertEqual(dy.capasity, 16)
        dy.delete(2)
        self.assertEqual(dy.count, 3)
        self.assertEqual(dy.capasity, 16)

    def test_delete2(self):
        dy = main.DynArray()
        for i in range(100):
            dy.append(i)
        self.assertGreater(dy.capasity, 100)
        for i in range(50):
            dy.delete(i)
        self.assertLess(dy.capasity, 70)

    def test_delete3(self):
        dy = main.DynArray()
        dy.append(1)
        dy.append(1)
        dy.append(1)
        self.assertEqual(dy.count, 3)
        dy.delete(10)
        self.assertEqual(dy.count, 3)