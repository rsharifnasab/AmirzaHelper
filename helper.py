import re

file1 = "list1.txt";
file2 = "list2.csv";

textfile = open(file2, 'r')
text = textfile.read()
textfile.close()
chars = input("pls enter your chars\n")
chars.replace(" ","") # removing white spaces
regex = "[" + str(chars) + "]{2,"+ str(len(chars)) +"}"
regex = re.compile(regex)
matches = re.findall(regex, text)
clean_matches = sorted(set(matches))

ans = ""
for w in clean_matches :
    ans = ans + w + "\n"
print(ans)

out_file = 'ans.txt'
out = open(out_file,'w')
out.write(ans)
out.close()

if len(matches) == 0 : print("no")
else : print("yeS")
