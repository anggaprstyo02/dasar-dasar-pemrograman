import math

def kubus(a):
    return 6*(a**2)

def balok(a,b,c):
    return 2*(a*b+a*c+b*c)

def tabung(a,b):
    return 2*math.pi*a*(a+b)

def prisma(a,b,c):
    l_alas=2*(0.5*a*b)
    l_selimut=3*a*c
    return l_alas+l_selimut

def limas(a,b,c):
    return (0.5*a*b)+(3*c)