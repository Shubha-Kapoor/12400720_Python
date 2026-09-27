import cmath
import math

a = int(input("enter value :"))
b = int(input("enter value :"))
c = int(input("enter value :"))

d = (b**2) - (4 * a * c)

# Handle real vs complex roots cleanly
if d >= 0:
    e = math.sqrt(d)
    x1 = (-b + e) / (2 * a)
    x2 = (-b - e) / (2 * a)
else:
    e = cmath.sqrt(d)
    x1 = (-b + e) / (2 * a)
    x2 = (-b - e) / (2 * a)

print(f"Roots of quadratic equation are: {x1} and {x2}")

"""
import cmath

# Input coefficients a, b, and c
a = int(input("enter value of a: "))
b = int(input("enter value of b: "))
c = int(input("enter value of c: "))

# Calculate the discriminant
d = (b**2) - (4 * a * c)

# CASE 1: d > 0 -> Discriminant is positive
# Results in two distinct, real roots
if d > 0:
    print("Case 1: d > 0 (Two distinct real roots)")
    e = d**(1/2)
    x1 = (-b + e) / (2 * a)
    x2 = (-b - e) / (2 * a)
    print("Roots are:", x1, "and", x2)

# CASE 2: d == 0 -> Discriminant is zero
# Results in real and equal roots (a single repeated root)
elif d == 0:
    print("Case 2: d = 0 (Real and equal roots)")
    x1 = -b / (2 * a)
    x2 = x1
    print("Roots are:", x1, "and", x2)

# CASE 3: d < 0 -> Discriminant is negative
# Results in complex/imaginary conjugate roots
else:
    print("Case 3: d < 0 (Complex conjugate roots)")
    e = cmath.sqrt(d)
    x1 = (-b + e) / (2 * a)
    x2 = (-b - e) / (2 * a)
    print("Roots are:", x1, "and", x2)"""