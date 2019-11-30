phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

temp = []
temp.extend(plist[1:3])
temp.append(plist[5])
temp.extend(plist[4:7:2])
temp.insert(4, plist[7])
plist = temp

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)