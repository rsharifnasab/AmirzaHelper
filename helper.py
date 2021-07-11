#!/usr/bin/python3
import re

word_list_list = ["list1.txt", "list4.txt", "list5.txt", "list6.txt"]
result_file = "ans.txt"


def check_count(found_word, chars):
    return True
    for c in found_word:
        for d in chars:
            if found_word.count(c) > chars.count(d):
                return False
    return True


chars = input("pls enter your chars\n").strip()

length = int(input("desired word length (-1 for any)\n"))

chars.replace("\\s+", "")  # removing white spaces

regex_str = "\\b[" + chars + "]{2,}\\b"
print(f"regex  : {regex_str}")


words = ""
for word_list in word_list_list:
    words += open(word_list, 'r').read().replace("\\s+", "\n")

regex = re.compile(regex_str)
matches = re.findall(regex, words)
uniq_matches = sorted(set(matches))

ans = ""
for match in uniq_matches:
    if length != -1 and len(match) != length:
        continue
    # if not check_count(match,chars):
    #    continue
    ans = f"{ans}{match}\n"

if ans == "":
    print("nothing found")
else:
    print(f"complete, saving to {result_file} . . ")

out = open(result_file, 'w')
out.write(ans)
out.close()
