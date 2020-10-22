
import math
a=int(input('a değerini giriniz:'))
b=int(input('b değerini giriniz: '))
c=int(input('c değerini giriniz: '))

delta=(b**2)-(4*a*c)

if(delta<2):
    print('Gerçel sayılarda kök yoktur.')
if(delta==0):
    x=(-b)/(2*a)
    print('Kökler çakışıktır.',x)
if(d>0):
    print('Gerçek iki kök vardır.')
    x1=((-b)+math.sqrt(delta)/(2*a) )
    x1 = ((-b)-math.sqrt(delta)/(2*a))
    print('x1:',x1)
    print('x1',x2)

print('sonuç',delta)