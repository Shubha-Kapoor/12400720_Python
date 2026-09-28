num = int(input("enter a value:"))
reverse = 0
original = num 
while num > 0:
    rem = num%10
    num = num//10
    reverse = (reverse * 10) + rem

if reverse==original:
    print("yes, number is pallindrome")
else:
    print("number is not pallindrome")