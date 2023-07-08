import unittest

class Doc:

    def __init__(self, string):
        self.string = string
        
    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __lt__(self, other):
        return len(self.string) < len(other.string)
    

class TestDoc(unittest.TestCase):
    def test_less_than(self):
        doc1 = Doc("what what")
        doc2 = Doc("hey hey")
        self.assertLess(doc2, doc1, "It's not less!")


if __name__ == '__main__':
    unittest.main()