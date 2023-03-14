a = 10
b = 5
c = 3

if(a>b and a<c):    # Only 1 condition is true and there is AND op, so it will not be evaluated.
    print("AND1")
if(a>b and a>c):    # Both condition are true, so it will be evaluated.
    print("AND2")

if(a>b or a<c):     # Only 1 condition is true and there is OR op, so it will still be evaluated.
    print("OR1")
if(a>b or a>c):     # Both condition are true, so it will be evaluated.
    print("OR2")

if(not(10>5)):      # 10 is greater than 5 but this If block's statement still won't get executed.
    print("Not operation.")