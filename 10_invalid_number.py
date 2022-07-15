number = int(input())
valid = bool
if 100 <= number <= 200 or number == 0:
    valid = False
else:
    valid = True
if valid:
    print("invalid")
