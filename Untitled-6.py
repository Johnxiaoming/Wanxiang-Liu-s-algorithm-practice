s1=raw_input("Enter string: ") #reading the string from user
s2=raw_input("Enter sub_string: ") #reading the sub_string from the user
l1=len(s1) #finding the length of the first string
l2=len(s2) #finding the length of the second string
print "sub_string occurences are:"
for i in range(0,l1-l2+1): #from each position checking for the occurence
    if(s1[i:i+l2]==s2):
        print i+1, #printing the occurence result