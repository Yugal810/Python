#To accept percentage and if percentage is greater than 90 (Grade A) and so on
p=int(input("Enter Percentage:"))
if p>=90:
    print("Grade A")
elif p>=80 and p<90:
    print("Grade B")
elif p>=60 and p<80:
    print("Grade C")
else:
    print("Fail")