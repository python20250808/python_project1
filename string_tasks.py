# wie viele Charaktere gibt es insgesamt?
# drucke Sonderzeichen.
# drucke text ohne Sonderzeichen.
# wie viele gibt es von den jeweiligen Sonderzeichen?
# wie viele gibt es von den jeweiligen Charakteren?

text = "hEl3lo? 3Worl8888d7 thi8s i8976/s m?7y FI=1RST= cO123456&de"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZßÄÖÜ "


spaceless_text = text.replace(" ", "")
print(spaceless_text)
print(f"length of the text: {len(spaceless_text)}") #1

'''
character = input("which character should be counted? ")
print(f"number of characters: {text.count(character.lower())}") #23
'''

'''
for index in range (0 , len(spaceless_text)):
    print(spaceless_text[index])
'''

'''
letters = ""
for ch in text.upper():
    if ch in alphabet:
        letters += ch
print(letters)

print(len(letters))
'''

counter = 0
special_character = ""
for ch in spaceless_text.upper():
    if ch not in alphabet:
        special_character += ch
        counter += 1

print(special_character)

print(counter)
#print(len(special_character))


