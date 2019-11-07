import random
#1
count = 8
def both():
    count = 1
    while count<=2:
        for a in range(8, -4, -1):
            print(a)
        count+=1
both()

#2
def is_odd():
    for a in range(1,10):
        if a%2 == 0:
            print("True")
        else:
            print("False")
        print(a)
is_odd()

#3
def dice_roll(x):
    y = 0
    count = 0
    while y == 0:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        count += 1
        if x == a + b + c:
            y += 1
    return count
print(dice_roll(17))
print(dice_roll(13))

#4

def odd_even_count(x):
    odd=0
    even=0
    while x>0:
        y=x%10
        if y%2==1:
           odd+=1
        else:
            even+=1
        x=int(x/10)
    z="odd: "+str(odd)+" even: "+str(even)
    return z
print(odd_even_count(2938270))


#5
def string_analysis(x):
    space=0
    number=0
    letter=0
    for i in x:
        if i ==" ":
            space+=1
        if i.isalpha()==True:
            letter+=1
        if i.isdigit()==True:
            number+=1
    z= "Space: "+str(space)+", Letter: "+str(letter)+", Number: "+str(number)
    return z
print(string_analysis("I'm not 89 years old"))













