import unittest
from complejos import *

class TestComplexNumbers(unittest.TestCase):
    def sumaTest(self):
        a,b = [1,2],[3,4]
        self.assertEqual(sumaC(a,b),(4,6))

    def productoTest(self):
        a,b = [1,2],[3,4]
        self.assertEqual(productoC(a,b),(-5,10))

    def restaTest(self):
        a,b = [1,2],[3,4]
        self.assertEqual(restaC(a,b),(-2,-2))
    
    def divisionTest(self):
        a,b = [1,2],[3,4]
        self.assertEqual(divisionC(a,b),(0.44,0.08))

    def moduloTest(self):
        a = [3,4]
        self.assertEqual(moduloC(a),5)
    
    def conjugadoTest(self):
        a = [3,4]
        self.assertEqual(conjugadoC(a),(3,-4))
    
    def polarACartesianaTest(self):
        r,p = 5,pi/2
        self.assertEqual(polarACartesiana(r,p),(0,5))
    
    def cartesianoAPolarTest(self):
        a = [3,4]
        self.assertEqual(cartesianoAPolar(a),(5,0.93))
    
    def faseTest(self):
        a = [3,4]
        self.assertEqual(faseC(a),0.93)

if __name__ == '__main__':
    unittest.main()
        