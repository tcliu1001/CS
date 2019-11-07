import cmath

#Q1
def mixed_number(a, b):
        whole_number = a // b
        numerator = a % b
        return str(whole_number) + " " + str(numerator) + "/" + str(b)

print(mixed_number(9, 2))

#Q2
def vowel_count_1(a):
        var1 = a.count('a')
        var2 = a.count('e')
        var3 = a.count('i')
        var4 = a.count('o')
        var5 = a.count('u')
        return var1 + var2 + var3 + var4 + var5
print(vowel_count_1('This is a sample'))


#Q3
def vowel_count_2(a):
    var1 = a.count('a')
    var2 = a.count('e')
    var3 = a.count('i')
    var4 = a.count('o')
    var5 = a.count('u')
    return var1, var2, var3, var4, var5
print(vowel_count_2('aeiou'))


#Q4
def sphere_volume(r):
    sphere_volume= 4/3 * (cmath.pi) * r**3
    return sphere_volume
print(sphere_volume(10))

def sphere_surface_area(r):
    sphere_surface_area = 4 * (cmath.pi) * r **2
    return sphere_surface_area
print(sphere_surface_area(10))

#Q5
def sphere_metrics(r):
    sphere_metrics = (sphere_surface_area(r), sphere_volume(r))
    return sphere_metrics
print(sphere_metrics(10))

#Q6
def name_function(name):
    name = ("Ted")
    age = 50
    weight = 80
    name_function = (name, age, weight)
    return name_function
print(name_function("Ted"))

#Q7
def rgb_to_hex(r, g ,b):
    r = hex(r)
    g = hex(g)
    b = hex(b)
    return r, g, b

print(rgb_to_hex(255, 0 , 0))


def hex_to_rgb(r, g, b):
    r= int(r, 16)
    g= int(g, 16)
    b= int(b, 16)
    return r, g, b
print(hex_to_rgb("ff", "00", "00"))


