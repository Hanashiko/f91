n = int(input())
def f91(number):
    if number <= 100:
        return f91(number + 1)
    elif number >= 101:
        return number-10
    
print(f91(n))
