
s = "Rob"
try:
    i = int(s)
except:
    i = -1
print(i)

rawstr = input("Enter a number: ")
try:
    ival = int(rawstr)
except:
    ival = -1

if (ival > 0):
    print("Good job!")
else:
    print("Not a number!")
