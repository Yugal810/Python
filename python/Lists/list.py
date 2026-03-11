mylist=["yugal","Ashish","Komal","Ankush",77,"Sandip",60.52,"YUGAL"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[1:8:2])
print(mylist[:])
print(mylist[::-1])

mylist.append('harsh')
mylist.append("laxman")
print(mylist)

mylist.insert(1,"sanket")
print(mylist)

mylist.remove("Sandip")
print(mylist)

newlist=mylist.copy()
print(mylist)
print(newlist)

