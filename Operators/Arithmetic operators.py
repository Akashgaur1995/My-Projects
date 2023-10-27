x= int(input("Enter First Number "))
y= int(input("Enter Second Number "))
a= x+y*y/x-y
print(a)
if (x+y)%2==0:  # Modular Sign is used to find even remainder
    print("Sum of two numbers is Even")
else:
    print("Sum of two numbers is Odd")
b=x//y      # // is used to find Quotient 
print("Quotient is", b)
c= x**y      # ** is used to put second no. as a power of first no.
print("x to the power y is ", c)