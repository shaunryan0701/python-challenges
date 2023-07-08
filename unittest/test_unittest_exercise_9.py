import unittest


class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only object of type str can be added to the list.')
        super().append(string)

class TestStringListOnly(unittest.TestCase):
    
    def test_append_string(self):
        slo = StringListOnly()
        slo.append("Bollox")
        self.assertIn("Bollox", slo)

    def test_append_not_string_should_raise_error(self):
        slo = StringListOnly()
        self.assertRaises(TypeError, slo.append, 55)
        self.assertRaises(TypeError, slo.append, True)

if __name__ == '__main__':
    unittest.main()