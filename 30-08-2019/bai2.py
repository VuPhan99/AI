Count = 0 
n = int(input('enter number '))
while(n != 0):
    n //= 10
    Count = Count +1
print('number of digits', Count)