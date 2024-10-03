#python program to make to simple calculator for two numbers
print('two numbers below:')
a=int(input('enter first number:'))
b=int(input('enter second number:'))
ch=0
while ch<5:
    print('calculator menu')
    print('1.add')
    print('2.subtract')
    print('3.multiply')
    print('4.divide')
    print('5.exit')
    ch=int(input('enter ur choice:'))

    if ch==1:
        c=a+b
        print('Sum',c)
    elif ch==2:
        c=a-b
        print('Difference:',c)
    elif ch==3:
        c=a*b
        print('Product:',c)
    elif ch==4:
        c=a/b
        print('quotient:',c)
    elif ch==5:
        break
    else:
        print('INVALID CHOICE')