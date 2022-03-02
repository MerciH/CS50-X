import cs50


    
while True:
    dollar = cs50.get_float("Change owed:")
    if dollar > 0:
        break
    
c = dollar * 100
c = round(c)
count = 0
while c >= 25:
    c -= 25
    count = count + 1
while c >= 10:
    c -=10
    count = count + 1
while c >= 4:
    c -= 4
    count = count + 1
while c >= 1:
    c -= 1
    count = count + 1
print(count)
    
