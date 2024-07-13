print('Enter the number of operation from the following , which do you want to perform : ')
A=input('''
        1.multiply,
        2.subtract,
        3.add,
        4.divide,
        5.reminder
        ''')
print('Enter first number =')
B=float(input())
print('Enter second number =')
C=float(input())
#B=float(B)
#C=float(C)

if A=='1':
     print(B*C)
elif A=='2':
        print(B-C)
elif A =='3':
        print(B+C)
elif A=='4':
        print(B/C)
elif A=='5':
        print(B%C)
else:
    print('invalid number of operation')