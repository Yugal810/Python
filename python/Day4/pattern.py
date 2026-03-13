#111
#222
#333
for i in range(1,4):
    for j in range(1,4):
        print(i, end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=" ")
    print()


n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-1):
        print("*",end=" ")
    print()