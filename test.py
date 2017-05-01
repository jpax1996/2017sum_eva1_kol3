import unittest
import matrix_module as mm

class test_mat(unittest.TestCase):

        def setUp(self):
	
                self.mat = mm.Matrix([1,1,1],[1,2,3])

        def test_add_mat(self):
	
                res = [[2,2,2],[2,4,6]]
                self.assertEqual(res, mm.Matrix.addition(self.mat,self.mat,self.mat))

        def test_mult_mat(self):
	
                res = [[1,1,1],[1,4,9]]
                self.assertEqual(res, mm.Matrix.multiplication(self.mat,self.mat,self.mat))

        def test_sub_mat(self):
	
                res = [[0,0,0],[0,0,0]]
                self.assertEqual(res, mm.Matrix.multiplication(self.mat,self.mat,self.mat))



if __name__==  '__main__':
	unittest.main()
