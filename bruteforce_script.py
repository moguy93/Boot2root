import os

charset = "123456"
combination = "6 5 4 3 2 1 \n"

for i in range(123456, 654321):
    err = False
    s = str(i)
    for j in charset:
        if s.count(j) != 1 or j == '0' or j > '6':
            err = True
            break
    if err == False:
        for c in s:
            combination += c + ' '
        combination += '\n'

answers="Public speaking is very easy.\n1 2 6 24 120 720\n0 q 777\n9\n?05+-1\n";

combs = combination.split('\n');

for i, comb in enumerate(combs):
    s = str(i)

    cmd_line1 = "print \"" + s + "\n" + comb + "\n\""
    cmd_line2 =  "\"" + answers + comb + "\n\"" + " > /tmp/exploit"
    # cmd_line3 = "/tmp/exploit | ./bomb 2&> /tmp/log ; grep -nr -E30 'Congratulations' /tmp/log" 
    os.system(cmd_line1)
    os.system(cmd_line2)
    os.system("chmod 777 /tmp/exploit")
    # os.system(cmd_line3)