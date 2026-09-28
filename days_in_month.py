a=int(input("enter a relevant number of month between 1-12:"))
if(a==1):
    print("january has 31 days")
elif(a==2):
    year=int(input("enter year in YYYY:"))
    if(year%4==0):
        print(f"february in {year} has 29 days")
    else:
        print(f"february in {year} has 28 days")
elif(a==3):
    print("March has 31 days")
elif(a==4):
    print("April has 30 days")
elif(a==5):
    print("May has 31 days")
elif(a==6):
    print("June has 30 days")
elif(a==7):
    print("July has 31 days")
elif(a==8):
    print("August has 31 days")
elif(a==9):
    print("September has 30 days")
elif(a==10):
    print("October has 31 days")
elif(a==11):
    print("November has 30 days")
elif(a==12):
    print("December has 31 days")
else:
    print("enter a valid value between 1-12")

