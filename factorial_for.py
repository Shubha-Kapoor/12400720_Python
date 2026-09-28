num = int(input("eneter num whose factorial we want:"))
factorial=1

for i in range(1,num+1):
    factorial=factorial*i
    num=num-1
print("factorial=",factorial)