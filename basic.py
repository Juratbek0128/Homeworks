##Begin1
a=int(input("tomonni kiriting:"))
p=int(4)*a
print("perimetri",p ,"ga teng")
##Begin2
a=int(input("tomonni kiriting:"))
S=a*a
print("yuzi",S ,"ga teng")
##Begin3
a=float(input("boyini kirting"))
b=float(input("enini kiriting"))
S=a*b
P=2*(a+b)
print("Tortburchak perimetri =\n", P)
print("Tortburchak yuzi",S)
##Begin4
d = 5
pi = 3.14
L = pi * d 
print("Aylananing uzunligi ", L)
##Begin5
a = 2
c = 3
d = 2
V = a**c
S = 6 * a**d
print("Hajmi", V, "To'lasirti ", S)
##Begin6
a = 2
b = 3
c = 4
V = a * b * c 
S = 2 * (a * b + b * c + c * a)
print("Hajmi ", V, "Yuzi ", S)
##Begin7
R = 5
L = 2 * pi * R 
S = pi * R * R 
print("Uzunligi ", L, "Yuzi ", S)
##Begin8
a = 1
b = 3
orta_arifmetik = (a + b)/2
print("O'rta arifmetigi", orta_arifmetik)
##Begin9
import math
a=int(input())
b=int(input())
g=math.sqrt(a*b)
print("o'rta geometrigi",g)
##Begin10
A = True
while A:
    a=int(input('A ni kiriting:'))
    if a == 0:
        print("Bu ammalni 0 bilan bajarib bo'lmaydi")
    else:
        A = False
B = True
while B:
            b = int(input('B ni kiriting:'))
            if b == 0:
                print("Bu ammalni 0 bilan bajarib bo'lmaydi")
            else:
                B = False
Y = a + b
K = a * b
A2 = a**2
B2 = b**2
print ("Yig'indi:", Y)
print ("Kupaytma:",K)
print ("kvadrati a:",A2 and "Kvadrati b:", B2)
##Begin11
import math
A = True
while A:
    a=int(input('A ni kiriting:'))
    if a == 0:
        print("Bu ammalni 0 bilan bajarib bo'lmaydi")
    else:
        A = False
B = True
while B:
            b = int(input('B ni kiriting:'))
            if b == 0:
                print("Bu ammalni 0 bilan bajarib bo'lmaydi")
            else:
                B = False
Y = a + b
K = a * b
A2 = math.fabs(a)
B2 = math.fabs(b)
print ("Yig'indi:", Y)
print ("Kupaytma:",K)
print ("moduli a:",A2) 
print("moduli b:", B2)
#Begin12
import math
a=int(input("a ni"))
b=int(input("b ni"))
c=a**2+b**2
c1=math.sqrt(c)
p=a+b+c
print("gipotenuza=",c1,"perimetri=",p)
#Begin13
R1 = float(input("Birinchi radiusni kiriting:"))
R2 = float(input("Ikkinchi radiusni kiriting:"))
S=3.14*(R1-R2)
print("Yuzalarining farqi shunga teng:" ,S )
#Begin14
L=int(input("L ni kiriting "))
Pi=3.14
l1=2*Pi*R
S1=Pi*R**2
print(l1,S1)
#Begin15
S=int(input("S ni kiriting "))
Pi=3.14
d=2*Pi*R
R=Pi*R**2
print(d,R)
#Begin16
import math
p = [3]
q = [1]
print (math.dist(p, q))
#Begin17
import math
a=[2]
b=[4]
c=[5]
ac=math.dist(a,c)
bc=math.dist(b,c)
print(ac, "\n" ,bc)
#Begin18
import math
a=[2]
b=[4]
c=[5]
ac=math.dist(a,c)
bc=math.dist(b,c)
k=ac*bc
print(k)
#Begin19
a=float(input("boyini kirting"))
b=float(input("enini kiriting"))
S=a*b
P=2*(a+b)
print(P,S)
#Begin20
import math
def shortest_distance(x1, y1, z1, a, b, c, d):
    d = abs((a * x1 + b * y1 + c * z1 + d))
    e = (math.sqrt(a * a + b * b + c * c))
    print("Perpendikulyar masofa", d/e)
x1 = 4
y1 = -4
z1 = 3
a = 2
b = -2
c = 5
d = 8
shortest_distance(x1, y1, z1, a, b, c, d)     
#Begin21
import math
a=[2]
b=[4]
c=[5]
ac=math.dist(a,c)
bc=math.dist(b,c)
k=ac*bc
print(k)
#Begin22
a=float(input("A son"))
b=float(input("B son"))
A=b
B=a
print(A,B)
#Begin23
a=float(input("A son"))
b=float(input("B son"))
c=float(input("B son"))
A=b
B=c
C=a
print(A,B,C)
#Begin24
a=float(input("A son"))
b=float(input("B son"))
c=float(input("B son"))
A=c
B=a
C=b
print(A,B,C)
#Begin25
x=int(input("X"))
y=3*x**6-6*x**2-7
print(y)
#Begin26
x=int(input("X"))
y=(x-3)**6-(x-3)**3
print(y)
#Begin27
a=int(input("A soni"))
a1=a**2
a2=a**4
a3=a**8
print(a1,a2,a3)
#Begin28
a=int(input("A soni"))
a1=a**2
a2=a**3
a3=a**5
a4=a**10
a5=a**15
print(a1,a2,a3,a4,a5)
#Begin29
pi = 22/7
degrees = 100
radians = degrees * pi / 180
print(radians)
##Begin30
import math
print("1 Radian darajaga teng: ", end ="")
print (math.degrees(1))
##Begin31
tf=int(input("Temperaturani kirizing:"))
tc=(tf-32)*5/9
print(tc)
##Begin32
tc=int(input("Temperaturani kirizing:"))
tf=(tc-32)*5/9
print(tf)
##Begin33
x="A"
B="1"+  "A"+   "Y"
print(B)
##Begin34
x=" A som"
y="  B som "
B=x+ y
print("1 kg konfet va shoolad " ,B)
##Begin35





