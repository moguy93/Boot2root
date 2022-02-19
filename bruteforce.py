from sys import stdout

charset = "123456"

for i in range(123456, 654321):
    err = False
    s = str(i)
    for j in charset:
        if s.count(j) != 1 or j == '0' or j > '6':
            err = True
            break
    if err == False:
        for c in s:
            stdout.write(c + ' ')
        stdout.write('\n')
