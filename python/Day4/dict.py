mydict={
    "name":"Alice"
}

mydict["age"]=30
print(mydict)

mydict.pop("age")
print(mydict)

mydict1={
    101:"Yugal",
    102:"Anish",
    103:"Swapnil",
    104:"Yash",
    105:"Joy"
}
for i,j in mydict1.items():
    print(i,"",j)