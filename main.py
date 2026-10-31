def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b):
    if b==0: raise ZeroDivisionError("Cannot divide by zero")
    return a/b

while True:
    c = input("1:Add 2:Sub 3:Mul 4:Div q:Quit > ")
    if c == 'q': break
    try:
        x = float(input("First: "))
        y = float(input("Second: "))
        if c=='1': print(x+y)
        elif c=='2': print(x-y)
        elif c=='3': print(x*y)
        elif c=='4': print(x/y)
    except Exception as e:
        print(f"Error: {e}")