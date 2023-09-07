# 1. + and ,
print ("Hi" + "Hello" + "Little" + "Baby")
print ("Hi", "Hello", "Little", "Baby")

# 2. Comments
# Single Line Comment
'''
This
is
a
Multi
Line
Comment
'''
"""
This is a Multi Line Comment but also a doc string
    * Used to tell what a function do
    * can be accessed using dunder / double under score / magical method / __doc__
"""

# 3. IDEs -> VScode, PyCharm, Sublime{good for simple, teaching & automation}, Shell{comes by default when installing python}

# 4. end, sep
print ("I", "am", "going", "to", sep='-', end='*****')
print ("use", "you")

# 5. _ or __ before a variable makes it private or protected (also in C++)

# 6.
x = 6
print(hex(id(x)))
print(id(x))
print(x)
x = 'hello'
print(hex(id(x)))
print(id(x))
print(x)
x = True
print(hex(id(x)))
print(id(x))
print(x)