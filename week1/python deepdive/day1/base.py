x = "Hello World"
print(f'Data: {x}, Type: {type(x)}')  #string text type
print(f'Data:{x},type:{type(x)}')
x=20                                    # integer numeric type
print(f'Data:{x},Type:{type(x)}')
x=20.5                                  # float type numeric type
print(f'Data:{x},Type:{type(x)}')
x=1+5j                                  # complex nnumeric type
print(f'Data:{x},Type:{type(x)}')
                                        #sequence types 
x=[1,2,3,"hi"]                          #list
print(f'Data:{x},Type:{type(x)}')
x=("banana","apple")                    #tuple        
print(f'Data:{x},Type:{type(x)}')
x=range(0,10)                           #Range
print(f'Data:{x},Type:{type(x)}')
x={"name":"jack","age":"23"}            # DIct Mapping type
print(f'Data :{x},Type: {type(x)}')
x={"name",33}                              #set type
print(f'Data:{x},Type:{type(x)}')
x=frozenset({"apple",345})                  #frozenset 
print(f'Data:{x},Type:{type(x)}')

x = True                                    #boolean
print(f'Data: {x}, Type: {type(x)}')

x = b"Hello"                                #Byte
print(f'Data: {x}, Type: {type(x)}')

x = bytearray(5)                            #byte array
print(f'Data: {x}, Type: {type(x)}')

x = memoryview(bytes(5))                    #memoryview
print(f'Data: {x}, Type: {type(x)}')

x = None                                    #None type
print(f'Data: {x}, Type: {type(x)}')


x = 1
y = 3565622255488771112222278967236573653756375637567365723657326592356327567365823
z = -3255522622255488771112222278967236573653756375637567365723657326592356327567365823
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.


print(type(x))
print(type(y))
print(type(z))

x=1.0
y=1.10
z=-1.4

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100
# Float can also be scientific numbers with an "e" to indicate the power of 10.

print(x, type(x))
print(y,type(y))
print(z,type(z))


# Types of Casting
# Explicit Casting (Type Conversion) → done manually using functions.
# Implicit Casting (Type Promotion) → done automatically by Python when safe.

x=1
y=3.2
z=x+y
print(z,type(z))

x="135"
a=int(x)
print(a,type(a))

a="     jayanth"
print(a[:-2])
print(a[::-1])
print(a[::-2])
print(a.upper())
print(a.lower())
print(a.replace('a', 'Mo'))
print(a)
print(a.lstrip())  #strip left side 
print(a.rstrip())  # strip using ,or any thing we gives
print(a.strip()) # strip the spaces

a="Rohith is noob man is that right "

print(a.split(' ', -1))
# It takes seperator and max number of splits, By default -1 equals to infinity
 
a="hello"
b="world"
c=a+b
print(c)

c=a+" "+b
print(c)


txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# List is a collection which is ordered and changeable. Allows duplicate members.
a=[1,2,3,1]

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
b=(1,4,2,1)
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
c={1,2,1,3}

# Dictionary is a collection which is ordered** and changeable. No duplicate members.
d={'a':'1','b':'4'}

print(a)
print(b)
print(c)
print(d)

li=['apple','banana','cat']
print(li)

for i in li:
    print(i)

for i in range(len(li)):
    print(li[i])

i=0
while i<len(li):
    print(li[i])
    i+=1

# newlist = [expression for item in iterable if condition == True]
new_li = [i for i in li if 'an' in i]
print(new_li)

new_li=[i for i in li if 'an' in i]
print(new_li)

list1 = [1,2,3]
list2 = list1 
list3=list1.copy()

list1.append(4)
print(list2)
print(list3)

list1=[1,34,5]
list2=list1
list3=list1.copy()

list1.append(4)

print(list1)
print(list2)
print(list3)