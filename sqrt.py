a=int(input("enter value :"))
b=int(input("enter value :"))
c=int(input("enter value :"))

d=(b**2)-(4*a*c)
e=d**(1/2)

x1=(-b+e)/2*a
x2=(-b-e)/2*a
print(f"root of quadratic equation with coefficients a,b &c are :",x1,"",x2)