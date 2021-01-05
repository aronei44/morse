def morse(kata):
        morseAlphabet ={
                "A" : ".-",             "B" : "-...",
                "C" : "-.-.",           "D" : "-..",            "E" : ".",
                "F" : "..-.",           "G" : "--.",            "H" : "....",
                "I" : "..",             "J" : ".---",           "K" : "-.-",
                "L" : ".-..",           "M" : "--",             "N" : "-.",
                "O" : "---",            "P" : ".--.",           "Q" : "--.-",
                "R" : ".-.",            "S" : "...",            "T" : "-",
                "U" : "..-",            "V" : "...-",           "W" : ".--",
                "X" : "-..-",           "Y" : "-.--",           "Z" : "--..",
                " " : "/"
        }
        key=[]
        kat = kata.upper()
        for k in kat:
                key.insert(len(key),k)
        for a in key:
                i = key.index(a)
                key[i] = morseAlphabet[a]


        return " ".join(key)
def kalimat(m):
        alphabet ={
                ".-":  "A",             "-...": "B",
                "-.-.":"C",             "-..":  "D",           ".":    "E",
                "..-.":"F",             "--.":  "G",           "....": "H",
                "..":  "I",             ".---": "J",           "-.-":  "K",
                ".-..":"L",             "--":   "M",           "-.":   "N",
                "---": "O",             ".--.": "P",           "--.-": "Q",
                ".-.": "R",             "...":  "S",           "-":    "T",
                "..-": "U",             "...-": "V",           ".--":  "W",
                "-..-":"X",             "-.--": "Y",           "--..": "Z",
                "/"   :" "
       }
        kta = m.split(" ")
        for a in kta:
                i = kta.index(a)
                kta[i] = alphabet[a]
        return "".join(kta).title()


while True:
        a = input("Masukan Kata / Kode Morse: ")
        if a[0] =="." or a[0] == "-":
                print(kalimat(a))
        else:
                print(morse(a))











                

