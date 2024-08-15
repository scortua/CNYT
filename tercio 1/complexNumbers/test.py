import unittest
from libraryComplex import *

class TestComplexNumbers(unittest.TestCase):
    def testSuma(self):
        a,b = [1,2], [3,4]
        c,d = [5,10], [3.5,9.1]
        self.assertAlmostEqual(sumaC(a,b), [4,6])
        self.assertAlmostEqual(sumaC(c,d), [8.5,19.1])

    def testProducto(self):
        a,b = [1,2], [3,4]
        c,d = [5,10], [3.5,9.1]
        self.assertAlmostEqual(productoC(a,b), [-5,10])
        self.assertAlmostEqual(productoC(c,d), [-77.5,55.5])

    def testResta(self):
        a,b = [1,2], [3,4]
        c,d = [5,10], [3.5,9.1]
        self.assertAlmostEqual(restaC(a,b), [-2,-2])
        self.assertAlmostEqual(restaC(c,d), [1.5,0.9])
    
    def testDivision(self):
        a,b = [1,2], [3,4]
        c,d = [5,10], [3.5,9.1]
        self.assertAlmostEqual(divisionC(a,b), [0.44,0.08])
        self.assertAlmostEqual(divisionC(c,d), [0.85,0.05])

    def testModulo(self):
        a = [3,4]
        d = [3.5,9.1]
        self.assertAlmostEqual(moduloC(a), 5)
        self.assertAlmostEqual(moduloC(d), 9.74)
    
    def testConjugado(self):
        a = [3,4]
        d = [3.5,9.1]
        self.assertAlmostEqual(conjugadoC(a), [3,-4])
        self.assertEqual(conjugadoC(d), [3.5,-9.1])  
    
    def testPolarACartesiana(self):
        r1,p1 = 5, pi/2
        r2,p2 = 2, pi/4
        self.assertAlmostEqual(polarACartesiana(r1,p1), [0,5])
        self.assertAlmostEqual(polarACartesiana(r2,p2), [1.41,1.41])
    
    def testcartesianoAPolar(self):
        a = [3,4]
        d = [3.5,9.1]
        self.assertAlmostEqual(cartesianoAPolar(a), [5,0.92])
        self.assertAlmostEqual(cartesianoAPolar(d), [9.5,1.19])
    
    def testFase(self):
        a = [3,4]
        d = [3.5,9.1]
        self.assertAlmostEqual(faseC(a), 0.92)
        self.assertAlmostEqual(faseC(d), 1.20)

if __name__ == '__main__':
    unittest.main()
        