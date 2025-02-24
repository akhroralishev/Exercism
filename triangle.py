def equilateral(sides): #teng tomonli uchburchak, hamma tomoni teng bo`ladi
    if len(sides) != 3 or any(side <= 0 for side in sides):
        return False
    return sides[0] == sides[1] == sides[2]
print(equilateral([3, 3, 3]))  # True
print(equilateral([3, 4, 5]))  # False


def isosceles(sides): #teng yonli uchburchak, 
    a, b, c = sides # sides = [1, 2, 3]
    if a < 0 or b < 0 or c < 0:
        return False
    if a + b < c:
        return False
    elif a + c < b:
        return False
    elif b + c < a:
        return False
    return a == b or a == c or b == c # ikita yoni teng bo`lishi kk,


print(isosceles([3, 3, 4]))  # True
print(isosceles([5, 5, 5]))  # False



def scalene(sides):  #har hil tarafli uchburchak
    a, b, c = sides  
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return len(set(sides)) == 3  

print(scalene([3, 4, 5]))  # True (Skalen uchburchak)
print(scalene([2, 2, 3]))  # False (Ikki tomoni teng)

