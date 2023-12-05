def f(x):
    return x*x*x


x=int(input(">"))

y1=(f(x)+f(1+x))/(3*f(x)+f(1+2*x+x**2))
y2=(2+f(2*x+1))**0.5

print("y1=",y1)
print("y2=",y2)
