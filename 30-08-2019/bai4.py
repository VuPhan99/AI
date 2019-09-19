string=input("Enter string:")
lower=0
upper=0
for i in string:
      if(i.islower()):
            lower = lower + 1
      elif(i.isupper()):
            upper = upper + 1
print("lowercase: ", lower)
print("uppercase: ", upper)