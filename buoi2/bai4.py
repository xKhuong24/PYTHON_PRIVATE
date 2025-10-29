e = input()
a = e.find("@")
b = e.find(".")
if a>0 and b >a+1 and b <len(e)-1:
    print("Valid")
else:
    print("Invalid")