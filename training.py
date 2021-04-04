def a(n):
    if len(str(n)) > 1:
        return n%10 + digital_root(int(n/10))
    else:
        return n
    
def digital_root(n):
    if len(str(n)) > 1:
        return a(n)
    else:
        return a(n)


print(digital_root(17))


