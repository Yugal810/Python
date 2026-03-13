for i in range(1,5):
    if i==3:
        break
    print(i)

for i in range(1,5):
    if i==3:
        continue
    print(i)


for i,j in zip(range(1,6), range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i,"",j)

i=1
while i<=5:
    print(i)
    i=i+1

username=""
password=""
while username != "admin" and password !="yugal":
    username= input("Enter username:")
    password= input("Enter password:")