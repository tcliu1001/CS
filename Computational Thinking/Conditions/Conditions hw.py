import random
min = 1
max = 6
def driving_age(x):
    if x>=18:
        print("True")
        return x
    else:
        print("False")
        return x
print(driving_age(16))
print(driving_age(20))


def id_triangle(a, b, c):
    if a**2+b**2 == c**2:
        print("right")
        return a, b, c
    if a**2 + b**2 < c**2:
        print("Obtuse")
        return a, b, c
    if a**2 + b**2 > c**2:
        print ("Acute")
        return a, b, c
    else:
        print("Not a triangle")
        return a, b, c
print(id_triangle(1,2,3))



def fizzbuz(x):
    if x//3>0 and x%3==0 and x//5>0 and x%5==0:
        return "FIZZBUZZ"
    elif x//3>0 and x%3==0:
        return "FIZZ!"
    elif x//5>0 and x%5==0:
        return "BUZZ!"
    else:
        print("Huh?")
        return "Huh?"
print(fizzbuz(12))


def guess_dice(a,b,c):
    x=random.randint(1,6)
    y=random.randint(1,6)
    z=random.randint(1,6)
    count=0
    if a == x:
        count = count + 1
    elif a == y:
        count = count + 1
    elif a == z:
        count = count + 1
    return "Rolled: " + str(x) + " " + str(y) + " " + str(z) + ", with " + str(count) + " correct"
print(guess_dice(1,4,5))


def gimme_random(type, a, b):
    if type == "int":
        a = int(a)
        b = int(b)
        num = int(random.randint(a, b))
        return num
    elif type == "float":
        num = float(random.uniform(a,b))
        return num
print(gimme_random("int", 2.3, 3))


























