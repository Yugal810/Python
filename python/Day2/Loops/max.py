#To accept five diff values in diff var and check max value and print by using simple "if statement"
p1=int(input("Enter Value 1:"))
p2=int(input("Enter Value 2:"))
p3=int(input("Enter Value 3:"))
p4=int(input("Enter Value 4:"))
p5=int(input("Enter Value 5:"))

if(p1>p2 and p1>p3 and p1>p4 and p1>p5):
    print("Max value:",p1)

elif (p2>p1 and p2>p3 and p2>p4 and p2>p5):
    print("Max value:",p2)

elif (p3>p1 and p3>p2 and p3>p4 and p3>p5):
    print("Max value:",p3)

elif (p4>p1 and p4>p2 and p4>p3 and p4>p5):
    print("Max value:",p4)

elif (p5>p1 or p5>p2 or p5>p3 or p5>p4):
    print("Max value:",p5)