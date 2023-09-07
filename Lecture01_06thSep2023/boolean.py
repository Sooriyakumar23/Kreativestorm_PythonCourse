# 1. Boolean Expressions
x = 5
y = 5

print(x == y)
print(x!=y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
print(x is y) # After 3.6 : only for int then true due to use of tuple of caching system from -5 to 255 & After 3.11 the range is even higher

# 2. Membership Check
print ('apple' in ['apple', 'orange', 'banana'])

# 3. Combination of Booleans
a = 5
b = 6
c = 7
print ((a < b) and (b < c))
print ((a < b) and (b > c))
print ((a < b) or (b < c))
print ((a < b) or (b > c))

# 4. IF conditions
x = 5
if (x > 0):
    print ("x is positive and", end=" ")
    if (x % 2 == 0):
        print ("even number")
    else:
        print ("odd number")
elif (x == 0):
    print ("x is ZERO !")
else:
    print ("x is negative")

# 5. Truthy & Falsy values
x = 42.0
if x:
    print ("This is Truthy")
y = 0.0
if (not(y)):
    print ("This is Falsy")

# 6.1. Exception
try:
    print (e)
except:
    pass
print('Done.....!')

# 6.2. Else in Exception
try:
    print (None)
except:
    pass
else:
    print ('ELSE block executes only if no exception occured / try block completely works')

# 6.3. Custom Exception
# i = -1
# if (i < 0):
#     raise Exception('No Negative Allowed')

# 6.4. Order Matters in Exception: Parent > Child
try:
    j = 1/0
except ArithmeticError:
    print ("Error in Arithmetically")
except ZeroDivisionError:
    print ("Error in Zero Divisionally")

try:
    j = 1/0
except ZeroDivisionError:
    print ("Error in Zero Divisionally")
except ArithmeticError:
    print ("Error in Arithmetically")

# 6.5. args in Exception
try:
    raise Exception("First", "Second")
except Exception as inst:
    print (type(inst))
    print (inst)
    print (inst.args)

    y, z = inst.args

    print (y)
    print (z)