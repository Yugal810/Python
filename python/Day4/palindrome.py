n="racecar"
rev = ""
for i in n:
        rev = i + rev
if rev==n:
        print("Palindrome")
else:
        print("Not a Palindrome")

#or 
#if n==n[::-1]:
#       print("Palindrome")
#else:
#       print("Not a Palindrome")