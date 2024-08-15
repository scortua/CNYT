from math import sqrt, atan2, sin, cos, pi
# a = (a1, a2) = a1 + a2i
# b = (b1, b2) = b1 + b2i

def sumaC(a,b):
    pReal = a[0] + b[0]
    pImag = a[1] + b[1]
    return [pReal,pImag]

def productoC(a,b):
    pReal = a[0]*b[0] - a[1]*b[1]
    pImag = a[0]*b[1] + a[1]*b[0]
    return [pReal,pImag]

def restaC(a,b):
    pReal = a[0] - b[0]
    pImag = a[1] - b[1]
    return [pReal,pImag]

def divisionC(a,b):
    pReal = (a[0]*b[0] + a[1]*b[1])/(b[0]**2 + b[1]**2)
    pImag = (a[1]*b[0] - a[0]*b[1])/(b[0]**2 + b[1]**2)
    return [pReal,pImag]

def moduloC(a):
    pModulo = sqrt(a[0]**2 + a[1]**2)
    return pModulo

def conjugadoC(a):
    pReal = a[0]
    pImag = -a[1]
    return [pReal,pImag]

def polarACartesiana(r,p):
    pReal = r*cos(p)
    pImag = r*sin(p)
    return [pReal,pImag]

def cartesianoAPolar(a):
    pModulo = moduloC(a)
    pFase = atan2(a[1],a[0])
    return [pModulo,pFase]

def faseC(a):
    fase = atan2(a[1],a[0])
    return fase    

'''
if __name__ == '__main__':
    a = (1,2)
    b = (3,4)
    print(sumaC(a,b))
    print(productoC(a,b))
    print(restaC(a,b))
    print(divisionC(a,b))
    print(moduloC(a))
    print(conjugadoC(a))
    print(polarACartesiana(2,pi/2))
    print(cartesianoAPolar(a))
    print(faseC(a))
'''
