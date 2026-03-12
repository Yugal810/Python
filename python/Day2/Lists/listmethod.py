list1=["Yugal","Anish"]
print(list1*2)

list2=[50,25.50]
print(list1+list2)

list3=[50,25.50,'Yugal']
del list3[1]
print(list3)

list4=[50,25,50,"Anish"]
list4.clear()
print(list4)

mylist=[44,22,77,0,9,88]
mylist.sort()
print(mylist)  # list should contain homogenius data otherwise we will geta type error

mylist.sort(reverse=True)
print(mylist)

math=10
phy=10   #python interpretor directly doesnt create another memory for same data, it first check whether the data exists or not, if not then creates another memory.
print(id(math))
print(id(phy))

mylist1=[44,22,77,0,9,88]
newlist=mylist   #alising means assigning one variable reference to another variable
print(id(mylist))
print(id(newlist)) #same address for both lists