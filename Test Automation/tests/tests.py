from .. import app 
import unittest

class TestClass(unittest.TestCase):
    def __init__(self,side):
        self.side=side
    def test_area(self):
        sq=app.Square(2)
        self.assertEqual(sq.area(),4, f'Area is shown {sq.area()} for side={sq.side} units')
if __name__== '__main__':
    unittest.main()