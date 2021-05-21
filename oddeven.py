#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If the check divides evenly into num, tell that to the user.
#If not, print a different appropriate message.

    
num=int(input("enter the first number:"))
check=int(input("enter the number to divide the first number by it:"))



if (num%check)==0:
    print(num,"is a multiple of",check)
else:
     print(num,"is not a multiple of",check)
