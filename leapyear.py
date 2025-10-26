import sys
def leapyrcla(yearinp):
    result=int(yearinp%4)
    if(result==0):
        seclogic(yearinp)
    else:
        print("Its not a leap year")

def seclogic(secvar):
    if(secvar%100!=0 or secvar%400==0):
        print("This is a leap year")
        sys.exit()
    else:
        print("This is not a leap year")

num=int(input("Please enter the year value:"))
if (num>0):
    leapyrcla(num)
else:
    print("Please enter a valid year")
