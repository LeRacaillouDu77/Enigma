def convert_cap(letter_int):
    if letter_int >= 97 and letter_int <= 122:
        letter_int = letter_int - 32
    return letter_int

def enigma(pos1, pos2, pos3, msg, dic):
    message = ""
    if pos1 <= 0 or pos1 > 26 or pos2 <= 0 or pos2 > 26 or pos3 <= 0 or pos3 > 26:
        print("default positions must be beetween 1 and 26.")
        return
    for letter in msg:
        if letter in dic:
            letter = dic[letter]
        letter_int = ord(letter)
        if letter_int >= 97 and letter_int <= 122 or letter_int >= 65 and letter_int <= 90:
            letter_int = convert_cap(letter_int) - 65
            letter_int = (letter_int + pos1 + pos2 + pos3) % 26 + 65
            if pos1 < 26:
                pos1 = (pos1 + 1) % 26
            if pos1 == 0:
                pos2 = (pos2 + 1) % 26
            if pos2 == 0:
                pos3 = (pos3 + 1) % 26
        if chr(letter_int) in dic:
            letter_int = ord(dic[chr(letter_int)])
        message += chr(letter_int)
    print(message)
    return message

def enigma_reverse(pos1, pos2, pos3, msg, dic):
    decoded_message = ""
    for letter in msg:
        if letter in dic:
            letter = dic[letter]
        letter_int = ord(letter)
        if letter_int >= 97 and letter_int <= 122 or letter_int >= 65 and letter_int <= 90:
            letter_int = (letter_int - 65 - pos1 - pos2 - pos3) % 26 + 65
            if pos1 < 26:
                pos1 = (pos1 + 1) % 26
            if pos1 == 0:
                pos2 = (pos2 + 1) % 26
            if pos2 == 0:
                pos3 = (pos3 + 1) % 26
        decoded_message += chr(letter_int)
    print(decoded_message)
    return message

def createDico(dic):
    chaine=input("Entrez les 2 lettres à échanger (exemple AE) ou rien pour quitter : \n--> ")
    while chaine !="":
        if chaine[0] not in dic :
            dic[chaine[0]]=chaine[1]
            dic[chaine[1]]=chaine[0]
        else:
            print("Lettre deja prise ")
        chaine=input("Entrez les 2 lettres à échanger (exemple AE) ou rien pour quitter : \n--> ")
    return dic

sens = input("encrypting or decrypting ? (encrypting by default) : ")
p1 = input("first rotor : ")
p2 = input("second rotor : ")
p3 = input("third rotor : ")
dic={}
createDico(dic)
message = input("message : ")
if sens == "":
    enigma(int(p1), int(p2), int(p3), message, dic)
else:
    enigma_reverse(int(p1), int(p2), int(p3), message, dic)
