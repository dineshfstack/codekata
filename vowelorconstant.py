ch11=input()
if(ord(ch1)==97 or ord(ch1)==101 or ord(ch1)==105 or ord(ch1)==111 or ord(ch1)==117 or ord(ch1)==65 or ord(ch1)==69 or ord(ch1)==73 or ord(ch1)==79 or ord(ch1)==85):
    print("Vowel")
elif((ord(ch1)>=65 and ord(ch1)<=90) or(ord(ch1)>=97 and ord(ch1)<=122)):
    print("Consonant")
else:
    print("invalid")