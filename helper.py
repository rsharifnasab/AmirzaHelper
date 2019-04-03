import re

file1 = "list1.txt";
file2 = "list2.csv";

textfile = open(file1, 'r')
text = textfile.read()
textfile.close()
chars = input("pls enter your chars\n")
chars.replace(" ","") # removing white spaces
regex = chars
matches = re.findall(regex, text)
print("mathc is : \n" ,matches)
if len(matches) == 0 : print("no")
else : print("yeS")
