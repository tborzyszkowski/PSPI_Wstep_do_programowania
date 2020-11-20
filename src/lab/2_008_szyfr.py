def encrypt(text, shift=10):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.isspace():
            result += char
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


def decrypt(text, shift=10):
    return encrypt(text, -shift)


tekst = "na straganie w dzien targowy takie slyszy sie rozmowy"

szyfr = encrypt(tekst, shift=2)

print(szyfr)

odszyfr = decrypt(szyfr, shift=2)

print(odszyfr)