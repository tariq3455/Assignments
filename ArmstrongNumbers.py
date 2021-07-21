num = input("Please enter a positive number: ")

total = 0

while not True:
    
    print("It is an invalid entry. Don't use non-numeric, float, or negative values! ")
    
    num = input("Please enter a positive number: ")
    
for i in num:
    
    total += int(i) ** int(len(num))
    
if total == int(num):
    print(total, "is a armstrong number")

else:
    print(num, "is not a armstrong number")