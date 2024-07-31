inpat = int(input("Enter number: "))

length = len(str(inpat))

a=0

for i in str(inpat):
    x=pow(int(i), length)
    a+=x

if (inpat == a):
    print('Armstrong number!', a)
else:
    print('Not an Armstrong number', a)
    
