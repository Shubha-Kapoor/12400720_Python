a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:"))

if a>b:
    if a>c:
        print(f"{a} is greatest")
    else:
        print(f"{c} is greatest")

else:
    if b>c:
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")