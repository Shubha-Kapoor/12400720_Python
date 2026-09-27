"""attendance = float(input("enter attendance %age:"))

if attendance >= 95.01:
    print("5 marks")
elif attendance >= 90.01:
    print("4 marks")
elif attendance >= 85.01:
    print("3marks")
elif attendance >= 80.01:
    print("2 marks")
elif attendance >= 75.01:
    print("1 marks")  
else:
    print("detain")"""

"""
A = float(input("enter attendance %age:"))
if A >=75:
    if A >= 95.01:
        print("5 marks")
    elif A >= 90.01:
        print("4 marks")
    elif A >= 85.01:
        print("3marks")
    elif A >= 80.01:
        print("2 marks")
    elif A >= 75.01:
        print("1 marks")  
else:
        print("detain")
 """

A = float(input("enter attendance %age:"))
if A>= 75:
    if A>=95.01:
        print("5 marks")
    else:
        if A>=90.01:
            print("4 marks")
        else:
            if A>=85.01:
                print("3 marks")
            else:
                if A>=80.01:
                    print("2 marks")
                else:
                    print("1 marks")
else:
    print("detain")
   

