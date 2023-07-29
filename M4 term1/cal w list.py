num = []
numlist = input().split(',')
num.append(numlist)
print(num)

numlist[0] = int(numlist[0])
numlist[2] = int(numlist[2])
if numlist[1] == "+":
    print(numlist[0], "+", numlist[2], "=", numlist[0]+numlist[2])

# subtract(-) two numbers
elif numlist[1] == "-":
    print(numlist[0], "-", numlist[2], "=", numlist[0]-numlist[2])

# multiplies(*) two numbers
elif numlist[1] == "*":
    print(numlist[0], "*", numlist[2], "=", numlist[0]*numlist[2])

# divides(/) two numbers
elif numlist[1] == "/":
    print(numlist[0], "/", numlist[2], "=", numlist[0]/numlist[2])

else:
    print("Invalid input")