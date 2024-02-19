# Basic Python Data Types

# String
print("Hello World!")
print("Hello World!"[4])
print("123" + "456")

# Int
print(5)
print(123_456_789)  # Interpreted as 123456789
print(123 + 456)

# Float
print(3.14159)
print(62.15 + 7)
print(123.456)

# Boolean
# Note: in Python, boolean are capitalized
print(True)
print(False)

namChar = len(input("What is your name?"))
print(type(namChar))
nameCharString = str(namChar)
print("Your name is " + nameCharString + " long.")