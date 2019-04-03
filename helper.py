import re

file1 = "list1.txt";
file2 = "list2.csv";

# ازبررگه
textfile = open(file2, 'r')
text = textfile.read()
textfile.close()

chars = input("pls enter your chars\n")
tool = int(input("enter tool : "))

chars.replace(" ","") # removing white spaces
regex = "[" + chars + "]{2,}"

regex = re.compile(regex)
matches = re.findall(regex, text)
uniq_matches = sorted(set(matches))

ans = ""
for w in uniq_matches :
    if len(w) != tool: continue;
    if (","+w+"\n") not in text : continue;
    ans = ans + w + "\n"

print(" working complete, saving to file..")

out_file = 'ans.txt'
out = open(out_file,'w')
out.write(ans)
out.close()

if ans == "" : print("nothing found")
else : print("wow, congradualtions")
