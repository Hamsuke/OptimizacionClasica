from sympy import *
from sympy.plotting import plot
from sympy.abc import x


e = 2.7182
def f1(x):
    return ((x**2)*(e**-x**2))

def f2(x):
    return (x**3)

def MaxMin(f):
    lista = []
    df = diff(f, x) # 1era. derivada
    d2f = diff(f, x, 2) # 2da. derivada
    pcs = solve(Eq(df,0)) # puntos críticos
    for p in pcs:
        if d2f.subs(x,p)>0:
            lista.append(p)
            tipo="Min"
        elif d2f.subs(x,p)<0:
            lista.append(p)
            tipo="Max"
        else:
            lista.append(p)
            tipo="Indefinido"
        print("x = %f (%s)"%(p,tipo))
    return lista

print("Ecuacion 1:")
funcion1=f1(x)
puntosx = MaxMin(funcion1)
puntosy = []
for y in puntosx:
    puntosy.append(f1(y))



plot(funcion1, (x, -2, 2),
                markers = [{'args': [puntosx,puntosy, 'b*']}],
                title="Ecuacion 1",
                line_color="red")


print("Ecuacion 2:")
funcion2=f2(x)
puntosx2=MaxMin(funcion2)
puntosy2 = []
for y in puntosx2:
    puntosy2.append(f2(y))
plot(funcion2, (x, -5, 5),
    markers = [{'args': [puntosx2,puntosy2, 'b*']}],
    title = "Ecuacion 2",
    line_color="red")