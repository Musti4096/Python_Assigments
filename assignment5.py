a = 0
b = 1
fibonacci = [a, b]
for i in range(1,10):
    c = a + b 
    fibonacci.append(c)
    a, b = b, c
 

print(fibonacci)
