n=int(input("Enter number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("The sum of first",n,"numbers is:",sum)


name="aaaaaaaabbbbcccc"
new=""
for i in name:
    if i not in new:
        new+=i
print(new)



