def one():
    try:print(int(input("num1:"))/int(input("num2:")))
    except ZeroDivisionError:print("ERROR:Division on 0 (even tho it's obviously going to be infinity since 1*∞=∞ and division is basically the opposite of multiplication)")
def two():
    try:print(int(input()))
    except ValueError:print("ERROR:Not a number")
def three():
    try:
        a=int(input())
        if a<0:raise SyntaxError()
    except SyntaxError:print("negative number")
    except ValueError:print("ERROR:NaN")
def four():
    try:
        def op(a,b,o):
            if o=="+":return a+b
            elif o=="-":return a-b
            elif o=="*":return a*b
            elif o=="/":return a//b
            else:print("ERROR:unknown operator")
        print(op(int(input()),int(input()),input()))
    except ZeroDivisionError:print("ERROR:infinity")
print("TRY:EXCEPT:")
while True:
    n=int(input("enter number:"))
    if n==1:one()
    elif n==2:two()
    elif n==3:three()
    elif n==4:four()
    else:print("unknown number")
