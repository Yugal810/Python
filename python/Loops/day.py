#Accept Days and check the working days and weekends

day=input("Enter the day")
if day=="Sunday" or day=="Saturday":
    print("Weekend")
elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Working Day")
else:
    print("Invalid day entered")