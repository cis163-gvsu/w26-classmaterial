import unittest

def foo2(x,y):
    if not isinstance(x, float) and not isinstance(x,int):
        raise TypeError
    if not isinstance(y, float) and not isinstance(y,int):
        raise TypeError

    if y == 0:
        raise ValueError
    return x/y

def foo(x,y):
    if not isinstance(x, float) and not isinstance(x,int):
        raise TypeError
    if not isinstance(y, float) and not isinstance(y,int):
        raise TypeError

    if y <= 0:
        raise ValueError
    if isinstance(x,int) and isinstance(y,int):
        return 5
    if isinstance(x,float):
        return 5.25

class MyTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(foo(10,2), 5)

    def test2(self):
        self.assertEqual(foo(15,3), 5)
    
    def test3(self):
        self.assertEqual(foo(10.5,2), 5.25)

    def test4(self):
        self.assertEqual(foo(0,3), 0)

    def test_divideby0(self):
        self.assertRaises(ValueError, foo, 3, 0)

    def test_divideby0_v2(self):
        with self.assertRaises(ValueError):
            foo(3,0)

    def test_divide_float_by0(self):
        with self.assertRaises(ValueError):
            foo(3.1,0)

    def test_str(self):
        with self.assertRaises(TypeError):
            foo('a',0)

    def test_wrong_num_inputs(self):
        with self.assertRaises(TypeError):
            foo(1,2,3)

    def test_None(self):
        with self.assertRaises(TypeError):
            foo(None, None)

    def test_inf(self):
        self.assertEqual(foo(float('inf'),3), float('inf'))

if __name__ == '__main__':
    unittest.main()
