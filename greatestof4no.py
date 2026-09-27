a = float(input("enter value of a:"))
b = float(input("enter value of b:"))
c = float(input("enter value of c:"))
d = float(input("enter value of d:"))

if a>b:
    if a>c:
        if a>d:
            print(f"{a} is greatest")
        else:
            print(f"{d} is greatest")
    else:
        if c>d:
            print(f"{c} is greatest")
        else:
            print(f"{d} is greatest")
elif b>a:
    if b>c:
        if b>d:
            print(f"{b} is greatest")
        else:
            print(f"{d} is greatest")
    else:
        if c>d:
            print(f"{c} is greatest")
        else:
            print(f"{d} is greatest")
elif c>a:
    if c>b:
        if c>d:
            print(f"{c} is greatest")
        else:
            print(f"{d} is greatest")
    else:
        if b>d:
            print(f"{b} is greatest")
        else:
            print(f"{d} is greatest")
elif d>a:
    if d>b:
        if d>c:
            print(f"{d} is greatest")
        else:
            print(f"{c} is greatest")
    else:
        if b>c:
            print(f"{b} is greatest")
        else:
            print(f"{c} is greatest")