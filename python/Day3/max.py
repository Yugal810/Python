#To accept three paper marks and check maximum marks using nested if else
p1=int(input("Enter Paper 1 marks:"))
p2=int(input("Enter Paper 2 marks:"))
p3=int(input("Enter Paper 3 marks:"))
if p1>p2:
    if p1>p3:
        print(p1, "is Max")
    else:
        print(p3, "is Max")

else:
    if p2>p3:
        print(p2,"is Max")
    else:
        print(p3, "is Max")