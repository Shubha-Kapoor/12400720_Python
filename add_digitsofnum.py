num = int(input("enetr a number:"))

sum = 0
while (num>0):
    rem = num%10 #remainder
    sum+=rem
    num=num//10
print(int(sum))
