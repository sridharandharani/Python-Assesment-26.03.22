import unittest
import program

class testforarmstrong(unittest.TestCase):

    def setUp(self):
        self.a = 371

    def tearDown(self):
        self.a = 0

    def test_armstrong(self):
        c = program.armstrongnum(self.a)
        self.assertTrue(c)

class testfordivisible(unittest.TestCase):

    def setUp(self):
        self.b = 100

    def tearDown(self):
        self.b = 0

    def test_divby5(self):
        c = program.divby5(self.b)
        self.assertTrue(c)

class testforlargest(unittest.TestCase):

    def setUp(self):
        self.a = 371
        self.b = 100
        self.c = 200

    def tearDown(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def test_largest(self):
        c = program.largest(self.a,self.b,self.c)
        self.assertEqual(self.a,c)

class testforevenorodd(unittest.TestCase):

    def setUp(self):
        self.a = 371
        self.b = 100

    def tearDown(self):
        self.a = 0
        self.b = 0

    def test_evenorodd1(self):
        c = program.check_EvenorOdd(self.a)
        self.assertFalse(c)

    def test_evenorodd2(self):
        c = program.check_EvenorOdd(self.b)
        self.assertTrue(c)



if __name__ == "__main__":
    unittest.main()