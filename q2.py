import numpy as np
import matplotlib.pyplot as plt



def bisection(f, a, b, accuracy):
    answerList = []
    while abs(a-b) > accuracy:
        midpoint = 0.5*a+0.5*b
        if f(midpoint) <0 and f(a)<0 or f(midpoint)>0 and f(a)>0:
            a = midpoint
        else: b = midpoint
    answerList.append(0.5*(a+b))
    return answerList

def newton(f, df, a, error):
    if abs(f(a)) < error:
        return a
    else:
        return newton(f, df, a-f(a)/df(a), error)

def secant(f,a,b,error):

    if abs(f(a)) <error:
        return a
    else:
        
        return secant(f,a-(a-b)*f(a)/(f(a)-f(b)),a, error)




"""f1 = lambda x: root.f1(x)
f2 = lambda x: root.f2(x)
f3 = lambda x: root.f3(x)
df1 = lambda x: (x+6/5)*(x+87/10)+(x-5/2)*(x+87/10)+(x-5/2)*(x+6/5)
df2 = lambda x: (2*np.cos(2*x)+1)/5
df3 = lambda x: x+2*np.cos(2*(x-4))-4
df4 = lambda x: np.cos(x)
df5 = lambda x:-1/(x**2)
#print(bisection(f3,3.6, 10,0.0001))
#print(newton(f3, df3, 3.6, 0.0001 ))

print(bisection(f4,-100, 11, 0.0001 )) #fails when osciliating
print(newton(f4,df4, 2, 0.001))

print((bisection(f5, -1, 1, 0.0001)))
print(newton(f5,df5,0,0.0001)) #Cannot divide by zero.
"""

f1 = lambda x: x**3-2*x**2-11*x +12
df1 = lambda x: 3*x**2 -4*x -11
b = []
for i in range(-5,5):
    b.append(newton(f1,df1, i, 1e-8))
c = np.zeros_like(b)

plt.plot(b,c)
plt.legend()






