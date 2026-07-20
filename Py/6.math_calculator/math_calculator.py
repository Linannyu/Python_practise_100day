from sympy import sqrt # 使用SymPy（符号数学库）。SymPy是一个用于符号数学的Python库，它支持许多符号数学运算，包括代数、微积分、方程求解等。在这里防止sqrt变成小数。
from sympy import cos, pi # 使用SymPy的cos函数和pi常量
from sympy import symbols, Eq, solve, sin, cos, tan, sympify # 使用SymPy的符号、方程和求解函数
from sympy import expand, pretty, factor # 使用SymPy的展开函数
import math

# Solve System of Equations
def Solve(sums, product):
    for a in range(-product,product + 1):
        for b in range(-product,product + 1):
                if a + b == sums and a * b == product:
                    print(a,b)
                    return a,b
                
# Pythagorean theorem(a**2 + b**2 = c**2)
def pythagorean(a = None, b = None, c = None):
    if a == None:
        a = sqrt(c**2 - b**2)
        print(a)
        return a
    elif b == None:
        b = sqrt(c**2 - a**2)
        print(b)
        return b
    elif c == None:
        c = sqrt(a**2 + b**2)
        print(c)
        return c
# 三角函数的计算
def trig(opposite = None, adjacent = None, hypotenuse = None, function = None):
    if function == 'sin' or function == 'sine':
         print(opposite / hypotenuse) 
         return opposite / hypotenuse
    elif function == 'cos' or function == 'cosine':
         print(adjacent / hypotenuse) 
         return adjacent / hypotenuse
    elif function == 'tan' or function == 'tangent':
         print(opposite / adjacent)
         return opposite / adjacent
    else:
        print('输入错误')


def trig_convert(opposite = None, adjacent = None, hypotenuse = None, to_function = None):
     if opposite is None:
         opposite = sqrt(hypotenuse**2 - adjacent**2)
     elif adjacent is None:
          adjacent = sqrt(hypotenuse**2 - opposite**2)
     elif hypotenuse is None:
          hypotenuse = sqrt(opposite**2 + adjacent**2)

     function = to_function
     trig(opposite, adjacent, hypotenuse, function)




special_angles = {
    30: {
        "sin": 1/2,
        "cos": sqrt(3)/2,
        "tan": sqrt(3)/3,
    },
    45: {
        "sin": sqrt(2)/2,
        "cos": sqrt(2)/2,
        "tan": 1,
    },
    60: {

        "sin": sqrt(3)/2,
        "cos": 1/2,
        "tan": sqrt(3),
    },
    90: {
        "sin": 1,
        "cos": 0,
        "tan": "undefined"
    }

}
# valueerence_angle 寻找参考角的象限和角度
def valueerence_angle(angle):
     # 取余，把任意角度转换成0-360度
     # %: a = b * (a // b) + (a % b)
     angle %= 360
     if 0 <= angle < 90: # quadrant I
          return angle,1
     elif 90 < angle < 180: # quadrant II
          return 180 - angle,2
     elif 180 < angle < 270: # quadrant III
          return angle - 180,3
     elif 270 < angle < 360: # quadrant IV
          return 360 - angle,4
     else:
          return None,0

# 输入函数值 -> 求反三角函
def inverse_trig(value = None,fun = None):
     if fun == 'sin':
          angle = math.degrees(math.asin(value))
     elif fun == 'cos':
          angle = math.degrees(math.acos(value))
     elif fun == 'tan':
          angle = math.degrees(math.atan(value))
     print(round(angle, 1))
     return round(angle, 1)

#  Special Angle Trigonometry 寻找特殊角值
def exact_value(function, angle):
     valueerence_angle(angle)
     value = special_angles[valueerence_angle(angle)[0]][function]
     quad = valueerence_angle(angle)[1]
     if function == 'sin' and quad in [1,2]:
          print(value)
          return value
     elif function == 'cos' and quad in [1,4]:
          print(value)
          return value
     elif function == 'tan' and quad in [1,3]:
          print(value)
          return value
     else:
          print(-value)
          return -value
def trig_equation_solution(fun, value):
     if fun =='sin':
          if value > 0:
               angles = [value, 180 - 180]
          elif value < 0:
               angles = [180 + value, 360 - value]
          else:
               angles = [0, 180]
     elif fun == 'cos':
          if value > 0:
               angles = [value, 360 - value]
          elif value < 0:
               angles = [180 - value, 180 + value]
          else:
               angles = [90, 270]
     elif fun == 'tan':
          if value > 0:
               angles = [value,value + 180]
          elif value < 0:
               angles = [180 - value, 360 - value]
          else:
               angles = [0, 180]
     # 保留一位小数
     print(sorted(round(angle, 1) for angle in angles))
# Linear Trigonometric Equations
def lte(fun = None,function = None, x = None):
     sol = solve(function, x)
     sol1 = inverse_trig(sol[0], fun)
     trig_equation_solution(fun, sol1)

def calu():
     x = symbols('x')
     y = symbols('y')
     meth = input('请输入您想使用的计算方法：')
     eq = input('请输入您想计算的方程：')

     if meth == 'expand':
          print(pretty(expand(eq)))
     elif meth == 'factor':
          print(pretty(factor(eq)))
     elif meth == 'solve':
          left, right = eq.split("=")
          eq = Eq(sympify(left), sympify(right))
          print(solve(eq, x))
     
     
# Solve(13, 42)
# trig(opposite=sqrt(26), hypotenuse=10, function='sin')
# b = pythagorean(a = 45,c = 53)
# trig_convert(opposite = 45, hypotenuse = 53, to_function = 'tan')
# exact_value('tan', 315) Exact Value of Trig Functions
'''
x = symbols('x')
# lte('tan', Eq(7*tan(x)-7, tan(x) - 3), tan(x))
y = symbols('y')
expr = (3*x-10)**2 - (x+1)**2
print(pretty(factor(expand(expr))))
calu()
'''
calu()