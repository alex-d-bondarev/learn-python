paranoid_android = "Marvin, the paranoid android"
letters = list(paranoid_android)
for letter in letters[:6]:
    print('\t', letter)
print()
for letter in letters[-7:]:
    print('\t'*2, letter)
print()
for letter in letters[12:20]:
    print('\t'*3, letter)