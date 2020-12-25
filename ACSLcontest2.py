import re
from difflib import SequenceMatcher
CommonSubs = []
NewSplit = []
input1 = (re.sub(r'[^a-zA-Z]', "", str(input("Enter your first string: ")))).upper()
input2 = (re.sub(r'[^a-zA-Z]', "", str(input("Enter your second string: ")))).upper()
split = [input1, input2]
num = 0
def longestSubstring(str1, str2):
    seqMatch = SequenceMatcher(None, str1, str2)
    match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))
    if (match.size != 0):
        return str1[match.a: match.a + match.size]
    else:
        return ''
def find_str(s, char):
    index = 0
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index
            index += 1
    return -1
longsub = longestSubstring(input1, input2)
CommonSubs.append(longsub)
index = find_str(split[0], longsub)
index2 = find_str(split[1], longsub)
split[0] = split[0].replace(longsub, '', 1)
split[1] = split[1].replace(longsub, '', 1)
print(split)
NewSplit.append(split[0][:index])
NewSplit.append(split[1][:index2])
NewSplit.append(split[0][index:])
NewSplit.append(split[1][index2:])
split = NewSplit
print(split)
NewSplit = []
while (len(split) >= 0):
    print(int(len(split)))
    for i in range(0, int(len(split)), 2):
        longsub = longestSubstring(split[i], split[i + 1])
        print(longsub)
        print(split[i])
        index = find_str(split[i], longsub)
        print(index)
        index2 = find_str(split[i + 1], longsub)
        split[i] = split[i].replace(longsub, '', 1)
        print(split[i])
        split[i + 1] = split[i + 1].replace(longsub, '', 1)
        print(split[i + 1])
        print(split)
        NewSplit.append(split[i][:index])
        NewSplit.append(split[i + 1][:index2])
        NewSplit.append(split[i][index:])
        NewSplit.append(split[i + 1][index2:])
        print(NewSplit)
        split = NewSplit
        NewSplit = []
print(split)

