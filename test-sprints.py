import unittest
import Sprints


class TestSprints(unittest.TestCase):
    def test_func(self):
        res1 = Sprints.MyFunc([23,345.6,23,56.7])
        self.assertEqual(res1, (23, 345.6)) 
        res2 = Sprints.MyFunc(["sdf"])
        self.assertEqual(res2, 0) 


if __name__ == "__main__"  :
    unittest.main() 
     