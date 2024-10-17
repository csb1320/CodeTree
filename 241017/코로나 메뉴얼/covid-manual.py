a = input().split()
b = input().split()
c = input().split()

if a[0] == 'Y' and b[0] =='Y' and c[0] == 'Y':
    if int(a[1]) >= 37:
        if int(b[1] >= 37):
            if int(c[1] >= 37):
                print('E')
            else:
                print('E')
        elif int(c[1] >= 37):
            if int(b[1] >= 37):
                print('E')
            else:
                print('E')
        else:
            print('E')
    else:
        print('E')

if a[0] == 'Y':
    if b[0] == 'Y':
        if int(a[1]) >= 37 and int(b[1]) >= 37:
            print('E')
        else:
            print('N')
    elif c[0] == 'Y':
        if int(a[1]) >= 37 and int(c[1]) >= 37:
            print('E')
        else:
            print('N')
    else:
        print('N')
elif b[0] == 'Y':
    if c[0] == 'Y':
        if int(b[1]) >= 37 and int(c[1]) >= 37:
            print('E')
        else:
            print('N')
    else:
        print('N')
else:
    print('N')