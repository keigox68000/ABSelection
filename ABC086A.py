a = input()
b, c = a.split(maxsplit=1)
if int(b) * int(c) % 2 == 0:
    print("Even") 
else:
    print("Odd")