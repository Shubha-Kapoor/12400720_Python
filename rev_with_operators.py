a = int(input("enter a 4 digit no.: "))
print("entered number is :", a)

# Extract individual digits
a1 = a % 10          # 1st digit from right (last digit)
s1 = a // 10         # remaining digits

a2 = s1 % 10         # 2nd digit from right
s2 = s1 // 10

a3 = s2 % 10         # 3rd digit from right
s3 = s2 // 10

a4 = s3 % 10         # 4th digit from right (first digit)

# Method A: Construct single reversed integer mathematically
rev_num = (a1 * 1000) + (a2 * 100) + (a3 * 10) + a4
print("the reverse of number", a, "is:", rev_num)

# Method B: Print extracted digits side-by-side using f-string
print(f"the reverse of number {a} is: {a1}{a2}{a3}{a4}")