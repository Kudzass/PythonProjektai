print('------------1: užduotis-----------------------')

def dalinti(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Dalyba iš nulio negalima."

print(dalinti(10, 2))
print(dalinti(5, 0))
print(dalinti(8, 4))
