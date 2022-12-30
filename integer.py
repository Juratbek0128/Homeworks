#Integer1
l=int(input("Uzunligini kirizing cm da:"))
m=l/100
print(f"{l} cm {m} metrga teng boladi ekan")
#Integer2
m=int(input("kg mi kiriting"))
t=m/1000
print(t,"tonna")
#Integer3
a=int(input("baytni kiriting"))
b=a/1024
print("{}bayt{}kb ga teng boladi".format(a,b))
#Integer4
a=int(input("a sonini kiriting"))
b=int(input("b sonini kiriting"))
if a>b:
    print(a/b)
elif a<b:
    print("xato son kirizdingiz")
#Integer5
a=int(input("a sonini kiriting"))
b=int(input("b sonini kiriting"))
if a>b:
    print((a-b)*100/a)
elif a<b:
    print("xato son kirizdingiz")
#Integer6
son = int(input("raqam kiriting"))
onlik =int((son // 10))
print(onlik)
birlik = int((son // 1))
print(birlik)
#Integer7
raqam = int(input("raqam kiriting"))
yigindi=raqam//10
yigindi1=raqam%10
yechim=yigindi+yigindi1
print(f"ikki xonali sonning raqamlari yig'indis {yechim}")
#Integer8
raqam = int(input("raqam kiriting"))
yigindi=raqam//10
yigindi1=raqam%10
print(f"{yigindi1}{yigindi}")
#Integer9
son = int(input("raqam kiriting"))
onlik =int((son // 10))
print(onlik)
birlik = int((son // 1))
print(birlik)
#Integer10
son = int(input("raqam kiriting"))
birlik = int((son // 1))
print(birlik)
onlik =int((son // 10))
print(onlik)
#Integer11
son = int(input("raqam kiriting"))
x=son//100 #3
x1=(son - x*100)//10
x2=son-x*100-x1*10
print(x+x1+x2)
#Integer12
son=str(124)
a=(son[::-1])
print(int(a))
#Integer13
a='123'.removeprefix('1')+'1'
#Integer14
a='123'.removeprefix('1')
a1='1'+a
print(a1)
#Integer15
a = input("son kiriting")
print ( a [ 1 ] + a [ 0 ] + a [ 2 ] )
#Integer16
a = input("son kiriting")
print ( a [ 0 ] + a [ 2 ] + a [ 1 ] )
#Integer17
son=999
x=son//100 
x1=(son - x*100)//10
x2=son-x*100-x1*10
print(x2)
#Integer18
son=9999
x1=son//1000 
x2=(son-(son % 1000))/1000  #%
print(int(x2))
#Integer19
n=240000000
a= n //60
print(a)
#Integer20
n=2400000
a= (n //60)//60
print(a)
#Integer21
n=240000000
a= n //60
b= n%60
print(a,b)
#Integer22
n = 123456789
h = ( n // 60 ) // 60
s = n % 60
print ( h ,  s )
#Integer23
n = 123456789
h = ( n // 60 ) // 60
m = ( n - ( h * 3600 ) ) // 60
s = n % 60
print ( h , m , s )
#Integer24
a=['yakshanba','Dushanba','seshanba','chorshanba','payshanba','juma','shanba']
k=int(10)
print(a[k%7])
#Integer25
a=['yakshanba','Dushanba','seshanba','chorshanba','payshanba','juma','shanba']
k=int(10)
print(a[k%7-3])
#Integer26
a=['yakshanba','Dushanba','seshanba','chorshanba','payshanba','juma','shanba']
k=int(10)
print(a[k%7-2])
#Integer27
a=['yakshanba','Dushanba','seshanba','chorshanba','payshanba','juma','shanba']
k=int(10)
print(a[k%7-0])
#Integer28
a=['yakshanba','Dushanba','seshanba','chorshanba','payshanba','juma','shanba']
k=int(2)
n=int(5)
print(a[k%7-n])
#Integer29
a=12
b=13245
c=10
A=(a//c)*(b//c)
print(A)
#Integer30
a=int(input("yilni kiriting"))
b=a//100
print(b+1)



