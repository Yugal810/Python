mydict={
    "name":"Yugal",
    "professional":"Developer",
    "empid":1001
}
print(mydict)
print(type(mydict))
print(id(mydict))

mydict1={
    101:"Yugal",
    102:"Anish",
    "103":"Swapnil",
    "104":"Yash",
    101:"Joy", # Updates 101 to Joy
    104:"Anish"  # This 104 is int therefore both "104":"Yash" and 104:"Anish" remains in the dictionary
}
print(mydict1)

#print value of specific key
a=mydict1[102]
print(a)

#change value of specific key
mydict1[102]="peter"
print(mydict1)

#printing keys of dictionary
for x in mydict1:
    print(x)

#printing vlaues of dictionary
for x in mydict1.values():
    print(x)

#printing both keys and values of dictionary
for x,y in mydict1.items():
    print(x,y)

#add new key and value in dictionary
mydict1["mobile_no"]=8395023198
print(mydict1)

#delete a key and value in dictionary
mydict2={
    101:"Yugal",
    "professional":"Developer",
    "empid":1001
}
mydict2.pop(101) #delete a key and value in dictionary by specific key
print(mydict2)

