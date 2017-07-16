#Carlos Justo
#Carlos Justo
#student number: 10369317
import unittest

from calculator1 import factorial
from calculator1 import add
from calculator1 import subtract
from calculator1 import multiply
from calculator1 import divide
from calculator1 import exponent
from calculator1 import squareroot
from calculator1 import square
from calculator1 import cube
from calculator1 import tang
from calculator1 import log
from calculator1 import sin 
from calculator1 import cos
from calculator1 import listcomp


class TestCalculator(unittest.TestCase):
	def testFactorial(self):
		self.assertEqual([720,120,40320],factorial([6,5,8]))
	


	def testAdd(self):
		self.assertEqual([6,10], add ([4,2],[2,8]))

				
	def testsubtract(self):
		self.assertEqual([2,-6], subtract ([4,2],[2,8]))
	
		
		
	def testmultiply(self):
		self.assertEqual([8,14], multiply ([2,2],[4,7]))
	
	def testdivide(self):
		self.assertAlmostEqual([1,1], divide ([7,9],[7,8])) # remenber to change
	
	
	def testexponent(self):	
		self.assertEqual([16,128], exponent ([2,2],[4,7]))
	
		
	def testsquareroot(self):	
		self.assertAlmostEqual([2,5,10,3], squareroot ([4,25,100,9]),places=2)
	
		
	def testsquare(self):
		self.assertEqual([16,9,64], square ([4,-3,8]))
	
	def testcube(self):
		self.assertEqual([64,343,729], cube ([4,7,9]))
	
	def testtang(self):
		self.assertEqual([0.9999999999999999,0.5773502691896257], tang ([45,30]))
		
		
	def testlog10(self):
		self.assertEqual([1.6532125137753437,1.0], log ([45,10])) 
	
		
	def testsin(self):
		self.assertEqual([1.0,0.49999999999999994,0.0], sin ([90,30,0]))
	
		
	def testcos(self):
		self.assertEqual([0.5000000000000001,0.8660254037844387,1.0], cos ([60,30,0]))
		
	def testlistcomp(self):
		self.assertEqual([(2,2),(4,4),(8,8)], listcomp ([1,10],[1,10]))
		
		
		
		

		
		
		
	#def testSubtract(self)
		
		
if __name__== '__main__':
	unittest.main()