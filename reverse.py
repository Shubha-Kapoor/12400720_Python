num = int(input("enter a value:"))
reverse=0

while num > 0:
    rem = num%10
    num = num//10
    reverse = (reverse * 10) + rem
print(reverse)