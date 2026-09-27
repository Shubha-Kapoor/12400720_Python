x1 = int(input("enter x1 coordinate of point A:"))
y1 = int(input("enter y1 coordinate of point A:"))

x2 = int(input("enter x2 coordinate of point B:"))
y2 = int(input("enter y2 coordinate of point B:"))
A = (x2-x1)**2
B = (y2-y1)**2
D = ( A + B )**(1/2)
print(f"Distance btw A and B is {D}")