#swapping Concept
#Swapping using temp Vraiable
a=100
b=150
print("Before swapping:")
print("a =", a)
print("b =", b)
temp=a
a=b
b=temp
print("After swapping:")
print("a =", a)
print("b =", b)
#swapping using without temp variable
print("Without using temp variable")
a = 100
b = 150
print("Before swapping:")
print("a =", a)
print("b =", b)
a,b=b,a
print("After swapping:")
print("a =", a)
print("b =", b)
#swapping using arithmetic operations
print("Using arithmetic operations")
a = 100
b = 150
print("Before swapping:")
print("a =", a)
print("b =", b)
a = a + b       #a = 100+150 = 250
b = a - b       #b = 250-150 = 100
a = a - b       #a = 250-100 = 150
print("After swapping:")
print("a =", a)
print("b =", b)
