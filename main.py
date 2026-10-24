x = 5 #int
y = 3.14 #float
name = "Alice" #string


#print(type(x))
#print(type(y))
#print(type(name))

a = 5
b = 2

print(f"Сумма {a / b}")
print(f"Сумма {a // b}")
print(f"Сумма {a % b}")


#opperation = input("введите опперацию(+, -, /, *):")

#if opperation == "+":
    #print(a + b)

#elif opperation == "-":
    #print(a - b)

#elif opperation == "/":
    #print(a / b)
   
#elif opperation == "*":
    #print(a * b)


for i in range(1, 5):
    print(i)


def add(x, y):
    if x<y:
       return x + y
    elif x>y:
        return x - y
    else:
        return "равенство"
    return (x + y)

print(add(a,b))

add_lambda = lambda x,y: x + y + 100
print(add_lambda(1,2))


print("all work")


