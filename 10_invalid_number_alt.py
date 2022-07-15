number = int(input())
valid = bool
if 100 <= number <= 200 or number == 0:
    ivalid = True
else:
    valid = False
if not valid:
    print("invalid")
