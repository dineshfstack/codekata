ch=input("Enter your character:")
if(ord(ch)==97 or ord(ch)=='101' or ord(ch)=='105' or ord(ch)=='111' or ord(ch)=='117' or ord(ch)=='65' or ord(ch)=='69' or ord(ch)=='73' or ch=='79' or ch=='85'):
    print("Vowel")
elif((ord(ch)>=65 and ord(ch)<=90) or(ord(ch)>=97 and ord(ch)<=122)):
    print("Consonant")
else:
    print("invalid")