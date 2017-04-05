import unittest
import matrix_module as mm

class test_mat(unittest.TestCase):

	def setUp(self):
	
		self.mat = mm.Matrix([1,1,1],[1,2,3])
	
	def test_add_mat(self):
	
		res = [2,2,2][2,4,6]
		self.assertEqual(res, self.mm.Matrix.addition(self.mat,self.mat))



if __name__==  '__main__':
	unittest.main()
