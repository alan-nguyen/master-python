def change(amount):
    d = amount % 5
    if d == 0:
        return [5] * int(amount/5)
    elif d == 1:
        return [7] * 3 + [5] * int((amount-21)/5)
    elif d == 2:
        return [7] + [5] * int((amount-7)/5)
    elif d == 3:
        return [7] * 4 + [5] * int((amount-28)/5)
    elif d == 4:
        return [7] * 2 + [5] * int((amount-14)/5)

# Test cases
print(change(24))
print(change(25))
print(change(26))
print(change(27))
print(change(28))
print(change(49))
