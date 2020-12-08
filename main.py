import random

def strigToArray(ar):
    arr = []
    for i in ar:
        arr.append(i)
    return arr

def encrypt(ar):
    text = ""
    key = random.randrange(20, 50)
    secondKey = random.randrange(4, 9)
    thirdKey = random.randrange(4,9)
    for i in ar:
        text = text + str(ord(i) * key) + "a"
    firstResult = text + str(key * secondKey)
    secondResult = text + str(key * secondKey) + str(secondKey) + "b"
    thirdResult = text + str(key * secondKey * thirdKey) + str(secondKey * thirdKey) + "b" + str(thirdKey) + "f"
    return thirdResult

def decrypt(ar):
    letters = []
    keys = []
    newLetters = []
    newKeys = []
    counter = -1
    letter = ""
    text = ""
    counter = -1
    asciiIntArray = []
    asciiCharArray = []

    for i in ar:
        text = text + i

        if i == "a":
            letters.append(text)
            text = ""
        if i == "b":
            keys.append(text)
            text = ""
        if i == "f":
            keys.append(text)
            text = ""
    for i in letters:
        newLetters.append(int(i.replace("a","")))
    for i in keys:
        newKeys.append(int(i.replace("b","").replace("f","")))

    thirdKey = newKeys[1]
    secondKey = int(strigToArray(str(newKeys[0]))[-2] + strigToArray(str(newKeys[0]))[-1])
    firstKey = int(str(str(newKeys[0]).replace(str(secondKey), "")))
    secondKey = int(secondKey / thirdKey)
    firstKey = int(firstKey / secondKey / thirdKey)
    for i in newLetters:
        asciiIntArray.append(i / firstKey)

    for i in asciiIntArray:
        asciiCharArray.append(chr(int(i)))

    for i in asciiCharArray:
        text = text + i

    return text

print("This is a encryption algorithm. Creator of this algorithm is Cem Boran Diribaş.")
print("Github: https://github.com/cemborandiribas")
print("Twitter: https://twitter.com/cemborandiribas")
print("Version: 0.1")
print()

req = str(input("If you want to encrypt a text please enter E, If you want to decrypt a text please enter D: "))

# or did not worked
if req == "e":
    text = str(input("Please enter your text: "))
    encrypted = encrypt(text)
    print("Your encrypted text is: ")
    print("**********")
    print(encrypted)

if req == "d":
    text = str(input("Please Input your encrypted text: "))
    decrypted = decrypt(text)
    print("Your decrypted text is: ")
    print("**********")
    print(decrypted)

if req == "E":
    text = str(input("Please enter your text: "))
    encrypted = encrypt(text)
    print("Your encrypted text is: ")
    print("**********")
    print(encrypted)

if req == "D":
    text = str(input("Please Input your encrypted text: "))
    decrypted = decrypt(text)
    print("Your decrypted text is: ")
    print("**********")
    print(decrypted)
# or did not worked
