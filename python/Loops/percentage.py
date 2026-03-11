#To accept three paper marks and calculate total , percentage and if oercentage is greater than equal to 60 than he or she is eligible for placemnet
p1=int(input("Enter Paper 1 marks:"))
p2=int(input("Enter Paper 2 marks:"))
p3=int(input("Enter Paper 3 marks:"))
total=p1+p2+p3
print(total)
per=(total/300)*100
print(per)
if per>=60:
    print("Eligible")
else:
    print("Not Eligible")