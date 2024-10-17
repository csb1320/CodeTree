a = input().split()
b = input().split()
c = input().split()

if a[0] == 'Y' and int(a[1]) >= 37:
    if(b[0] == 'Y' and int(b[1]) >= 37) or (c[0] == 'Y' and int(c[1]) >= 37):
        print('E')
    else:
        print('N')
else:
    if(b[0] == 'Y' and int(b[1]) >= 37) and (c[0] == 'Y' and int(c[1]) >= 37):
        print('E')
    else:
        print('N')