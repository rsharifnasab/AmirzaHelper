#!/usr/bin/python3
import re

def is_count_ok(found_word,chars):
    for c in found_word:
        for d in chars:
            if found_word.count(c) > chars.count(d) : return False;
    return True;

file = "list4.txt";
textfile = open(file, 'r')
text = textfile.read()
textfile.close()


chars = input("pls enter your chars\n")
tool = -1
tool = int(input("enter tool : (-1 for all) \n"))

chars.replace(" ","") # removing white spaces

regex = "[" + chars + "]{2,}"
regex = re.compile(regex)
matches = re.findall(regex, text)
uniq_matches = sorted(set(matches))

ans = ""
for match in uniq_matches :
    if (tool != -1)  and (len(match) != tool): continue
    if f",{match}\n" not in text : continue
    if not is_count_ok(match,chars) : continue;
    ans = ans + match + "\n"

print(" working complete, saving to file . . ")

out_file = 'ans.txt'
out = open(out_file,'w')
out.write(ans)
out.close()

if ans == "" : print("nothing found")
else : print("wow, congradualtions")
