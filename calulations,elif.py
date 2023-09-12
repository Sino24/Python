print("1 add")
print("2 sub")
print("3 mult")
print("4 div")
c=int(input("enter a choice"))
a=int(input("enter a no1"))
b=int(input("enter a no2"))
if c==1:
    result=a+b
    print("ans is",result)
elif c==2:
    result=a-b
    print("ans is")
elif c==3:
    result=a*b
    print("ans is")
elif c==4:
    result=a/b
    print("ans is")
else:
    print("invalid")
