a=50
b=30
c=20
d=10
print(int((a+b)*c/d))
print(int((a-b)*(c/d)))
print(int(a+(b*c)/d))

x=['A','B','C']
y=['A','B','C']
z=[1,2,3,4]
print(x==y)
print(x==z)
print(x!=z)

#no of consonants and vowels
n="YugalSonparateU"
name=n.lower()
data=['a','e','i','o','u']
vowel=0
cons=0
for i in name:
    if i in data:
        vowel=vowel+1
    else:
        cons=cons+1
print(vowel)
print(cons)
