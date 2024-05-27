# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")


score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# The modulo % operator in programming allows one to see if two numbers divide evenly or divide and have a remainder.
# For example, 4 % 2 would result in zero, because it evenly divides. However, 3 % 2 does not divide evenly and would result in a number other than zero!

z = int(input("What's z? "))

if z % 2 == 0:
    print("Even")
else:
    print("Odd")

#then we can create our own function by adjusting the code to:

def main():
    w = int(input("What's w? "))
    if is_even(w):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

#then we can make it more "pythonic" which is unique to python code by revising it to make it more readable

def main():
    l = int(input("What's l? "))
    if is_even(l):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0

main()

# match statements can be used to conditionally run code that matches certain values.


#example using if, elif, and else

name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron": 
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

#example using match statements

person = input("What's your name? ")

match person: 
    case "Harry" | "Hermione" | "Ron": #the | are similar to the 'or' keyword
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: #the _ symbol results in similar behavior to an 'else' statement
        print("Who?")