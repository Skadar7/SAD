import os
import docx

file = open("te.txt", "r")
doc  = docx.Document()
all_tb = [12]
for i in range(len(all_tb)):
    all_tb[i] = doc.add_table(rows=1, cols=44)
    all_tb[i].style = 'Table Grid'

while True:
    line = file.readline()
    if not line:
        break
    for q in range(len(all_tb)):
        rC[i].text = line[i]

doc.save('table.docx')
os.system("start table.docx")


