import unittest
from libraryComplex import *

class TestComplexNumbers(unittest.TestCase):
    def testSuma(self):
        a,b = [2,3], [4,5]
        c,d = [1,-2], [3,4]
        self.assertEqual(sumaC(a,b), [6,8])
        self.assertEqual(sumaC(c,d), [4,2])

    def testProducto(self):
        a,b = [1,2], [3,4]
        c,d = [5,10], [3.5,9.1]
        self.assertEqual(productoC(a,b), [-5,10])
        self.assertEqual(productoC(c,d), [-73.5,80.5])

    def testResta(self):
        a,b = [2,3], [1,4]
        c,d = [1,2], [3,5]
        self.assertEqual(restaC(a,b), [1,-1])
        self.assertEqual(restaC(c,d), [-2,-3])
    
    def testDivision(self):
        a,b = [3,4], [1,2]
        c,d = [5,6], [3,4]
        self.assertEqual(divisionC(a,b), [2.2,-0.4])
        self.assertEqual(divisionC(c,d), [1.56,-0.08])

    def testModulo(self):
        a = [3,4]
        d = [8,-6]
        self.assertEqual(moduloC(a), 5)
        self.assertAlmostEqual(moduloC(d), 10)
    
    def testConjugado(self):
        a = [3,4]
        d = [3.5,9.1]
        self.assertEqual(conjugadoC(a), [3,-4])
        self.assertEqual(conjugadoC(d), [3.5,-9.1])  
    
    def testPolarACartesiana(self):
        r1,p1 = 5, 0.9272952180016122
        r2,p2 = 9.749871794028882, 1.2036224929766774
        self.assertEqual(polarACartesiana(r1,p1), [3,4])
        self.assertEqual(polarACartesiana(r2,p2), [3.5,9.1])
    
    def testcartesianoAPolar(self):
        a = [3,4]
        d = [3.5,9.1]
        self.assertEqual(cartesianoAPolar(a), [5,0.9272952180016122])
        self.assertEqual(cartesianoAPolar(d), [9.749871794028882,1.2036224929766774])
    
    def testFase(self):
        a = [3,4]
        d = [3.5,9.1]
        self.assertEqual(faseC(a), 0.9272952180016122)
        self.assertEqual(faseC(d), 1.2036224929766774)

if __name__ == '__main__':
    unittest.main()
        