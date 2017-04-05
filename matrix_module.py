class Matrix:
		
	def __init__(self, matrix_1, matrix_2):
		self.matrix_1 = matrix_1
		self.matrix_2 = matrix_2
	
	
	def addition(self, matrix_1, matrix_2):
		matrix_3 = []									#the result matrix
		
		if (len(matrix_1) > 1) & (len(matrix_2) > 1):	#operation between matrices
		
			for i in range(4):
				res = matrix_1[i] + matrix_2[i]
				matrix_3.append(res)
			return matrix_3
			
		elif len(matrix_1) == 1:						#operation between scalar and matrix
			for i in range(4):
				res = matrix_1[0] + matrix_2[i]
				matrix_3.append(res)
			return matrix_3
			
		else:											#operation between matrix and scalar
			for i in range(4):
				res = matrix_1[i] + matrix_2[0]
				matrix_3.append(res)
			return matrix_3			
	
	
	def multiplication(self, matrix_1, matrix_2):
		matrix_3=[]
		index = 0
		
		for i in range(0,4,2):
			for j in range (2):
				res = matrix_1[i] * matrix_2[j] + matrix_1[i+1] * matrix_2[j+2]
				matrix_3.insert(index , res)
				index = index + 1
		return matrix_3


	def subtraction(self, matrix_1, matrix_2):
		matrix_3 = []									#the result matrix
		
		if (len(matrix_1) > 1) & (len(matrix_2) > 1):
				
			for i in range(4):
				res = matrix_1[i] - matrix_2[i]
				matrix_3.append(res)
			return matrix_3
			
		elif len(matrix_1) == 1:
			for i in range(4):
				res = matrix_1[0] - matrix_2[i]
				matrix_3.append(res)
			return matrix_3
			
		else:
			for i in range(4):
				res = matrix_1[i] - matrix_2[0]
				matrix_3.append(res)
			return matrix_3	
