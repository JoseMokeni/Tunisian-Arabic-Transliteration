from openpyxl import load_workbook
import easygui
import pyperclip

buck2uni = {
    "}": u"\u0621", # hamza-on-the-line
    "#": u"\u0623", # hamza-on-'alif
    "&": u"\u0624", # hamza-on-waaw
    "<": u"\u0625", # hamza-under-'alif
    "|": u"\u0622", # 'alif madda آ
    "{": u"\u0626", # hamza-on-yaa'
    
    
    ">": u"\u0629", # taa' marbuuTa
    
    
    "ā" : u"\u0627", # bare 'alif
    "ạ" : u"\u0627", # bare 'alif
    "ä": u"\u0627", # bare 'alif
    "æ": u"\u0627", # bare 'alif
    "a̦" : u"\u0649", # 'alif maqSuura
    "b" : u"\u0628", # baa'
    "b̄" : u"\u0628\u0651", # baa' with shadda
    "t" : u"\u062a", # taa'
    "t̄" : u"\u062a\u0651", # taa' with shadda
    "T" : u"\u062b", # thaa'
    "T̄" : u"\u062b\u0651", # thaa' with shadda
    "p" : u"\u067e", # paa'
    "p̄" : u"\u067e\u0651", # paa' with shadda
    "j" : u"\u062c", # jiim
    "j̄" : u"\u062c\u0651", # jiim with shadda
    "ꜧ" : u"\u062D", # Haa'
    "ꜧ̄" : u"\u062D\u0651", # Haa' with shadda
    "ḳ" : u"\u062e", # khaa'
    "ḳ̄" : u"\u062e\u0651", # khaa' with shadda
    "d" : u"\u062f", # daal
    "d̄" : u"\u062f\u0651", # daal with shadda
    "ḏ" : u"\u0630", # dhaal
    "ḏ̄" : u"\u0630\u0651", # dhaal with shadda
    "r" : u"\u0631", # raa'
    "r̄" : u"\u0631\u0651", # raa' with shadda
    "z" : u"\u0632", # zaay
    "z̄" : u"\u0632\u0651", # zaay with shadda
    "s" : u"\u0633", # siin
    "s̄" : u"\u0633\u0651", # siin with shadda
    "ṡ" : u"\u0634", # shiin
    "ṡ̄" : u"\u0634\u0651", # shiin with shadda
    "ṣ" : u"\u0635", # Saad
    "ṣ̄" : u"\u0635\u0651", # Saad with shadda
    "ḍ" : u"\u0636", # Daad
    "ḍ̄" : u"\u0636\u0651", # Daad with shadda
    "ṭ" : u"\u0637", # Taa'
    "ṭ̄" : u"\u0637\u0651", # Taa' with shadda
    "Z" : u"\u0638", # Dhaa'
    "Z̄" : u"\u0638\u0651", # Dhaa' with shadda
    "з" : u"\u0639", # 3ayn
    "з̄" : u"\u0639\u0651", # 3ayn with shadda
    "ġ" : u"\u063a", # ghayn
    "ġ̄" : u"\u063a\u0651", # ghayn with shadda
    "f" : u"\u0641", # faa'
    "f̄" : u"\u0641\u0651", # faa' with shadda
    "q" : u"\u0642", # qaaf
    "q̄" : u"\u0642\u0651", # qaaf with shadda
    "k" : u"\u0643", # kaaf
    "k̄" : u"\u0643\u0651", # kaaf with shadda
    "g" : u"\u06A8", # gaaf
    "ḡ" : u"\u06A8\u0651", # gaaf with shadda
    "v" : u"\u06A5", # vaaf
    "v̄" : u"\u06A5\u0651", # vaaf with shadda
    "l" : u"\u0644", # laam
    "l̄" : u"\u0644\u0651", # laam with shadda
    "m" : u"\u0645", # miim
    "m̄" : u"\u0645\u0651", # miim with shadda
    "n" : u"\u0646", # nuun
    "n̄" : u"\u0646\u0651", # nuun with shadda
    "н" : u"\u0647", # haa'
    "н̄" : u"\u0647\u0651", # haa' with shadda
    "w" : u"\u0648", # waaw
    "ō" : u"\u0648", # waaw
    "w̄" : u"\u0648\u0651", # waaw with shadda
    "y" : u"\u064A", # yaa'
    "ī" : u"\u064A", # yaa'
    "ȳ" : u"\u064A\u0651", # yaa' with shadda
    
    
    
    "a": u"\u064E", # fatHa
    "o": u"\u064F", # Damma
    "i": u"\u0650", # kasra
    "?" : u"\u061F", # question mark
    "," : u"\u060C", # comma
    "%" : u"\u066A", # percent
    ";" : u"\u061B", # semicolon
    
    # shadda = ~
    "~" : u"\u0651", # shadda
}

specialChars = ["?", ",", "!", ":", ";", "%"]

def transString(string, reverse=1):
    '''Given a Unicode string, transliterate into Buckwalter. To go from
    Buckwalter back to Unicode, set reverse=1'''

    for k, v in buck2uni.items():
        # if the word contains non-back2uni characters, skip it
        # if k not in string:
        #     continue
        if not reverse:
            string = string.replace(v, k)
        else:
            string = string.replace(k, v)

    return string


def transliterate(word):
    # trim ending spaces
    word = word.strip()
    
    
    # todo: fix this by treating the case of ending spaces
    if " " in word:
        splittedWord = word.split(" ")
        firstWord = splittedWord[0]
        rest = " ".join(splittedWord[1:])
        if firstWord != "":
            return transliterate(firstWord) + " " + transliterate(rest)
        else:
            return transliterate(" ".join(splittedWord[1:]))
    
    # check if there is a special character in the end of the word
    if word[-1:] in specialChars:
        specialChar = word[-1:]
        trueWord = word[:-1]
        return transliterate(trueWord) + transString(specialChar)
    
    # check if there is a special character in the beginning of the word
    if word[:1] in specialChars:
        specialChar = word[:1]
        trueWord = word[1:]
        return transString(specialChar) + transliterate(trueWord)
        
    if "\"" in word:
        if ("-" in word):
            firstPart = word.split("-")[0]
            secondPart = word.split("-")[1]
            # trim th \" at the beginning and end of the second part
            secondPart = secondPart[1:-1]
            firstLetterOfFirstPart = firstPart[0]
            if (firstLetterOfFirstPart != "e"):
                return transliterate(f"{firstLetterOfFirstPart}æl") + secondPart
            else: 
                return transliterate("æl") + secondPart
        else:
            # trim th \" at the beginning and end of the word
            word = word[1:-1]
            return word
    
    # ey
    if word == "ey":
        word = "æy"
    # eyh
    if word == "eyh":
        word = "æyн"
        
    # =================== BARE ALIF ====================
    word = word.replace("ā", "ä")
    # print("After ä replacement ", list(word))
        
    # =================== TAA MARBUTA ===================
    # if the word ends with "a" replace it with ">"
    if word[-1:] == "a":
        word = word[:-1] + ">"
        
    # YAA AND WAW
    
    # if the word begins with "'ī" replace it with "<y"
    if word[:3] == "'ī":
        word = "<y" + word[3:]
        
    # if the word begins with "ii" replace it with "<y"
    if word[:2] == "ī":
        word = "<y" + word[2:]

        
    # if the word begins with "'oo" replace it with "#w"
    if word[:3] == "'ō":
        word = "#w" + word[3:]

    # if the word begins with "oo" replace it with "#w"
    if word[:2] == "ō":
        word = "#w" + word[2:]

        
    
    # replace ō with w
    if ("ō" in word):
        word = word.replace("ō", "w")
    # replace ī with y
    if ("ī" in word):
        word = word.replace("ī", "y")

    # =================== HAMZA ===================


    # if the word begins with "'a" replace it with "#a"
    if word[:2] == "'a":
        word = "#a" + word[2:]
    # if the word begins with "a" replace it with "#a"
    if word[:1] == "a":

        word = "#a" + word[1:]
        
    # if the word begins with "'o" replace it with "#o"
    if word[:2] == "'o":
        word = "#o" + word[2:]
    # if the word begins with "o" replace it with "#o"
    if word[:1] == "o":
        word = "#o" + word[1:]
        
    # if the word begins with "'i" replace it with "<i"
    if word[:2] == "'i":
        word = "<i" + word[2:]
    # if the word begins with "i" replace it with "<i"
    if word[:1] == "i":
        word = "<i" + word[1:]
        
    # if the word begins with "'ä" replace it with "|"
    if word[:2] == "'ä":
        word = "|" + word[2:]
    # if the word begins with "ä" replace it with "|"
    if word[:1] == "ä":
        word = "|" + word[1:]
        
    
        
    # # if the word begins with "'ii" replace it with "<y"
    # if word[:3] == "'ii":
    #     word = "<y" + word[3:]
    # # if the word begins with "ii" replace it with "<y"
    # if word[:2] == "ii":
    #     word = "<y" + word[2:]
        
    # # if the word begins with "'oo" replace it with "#w"
    # if word[:3] == "'oo":
    #     word = "#w" + word[3:]
    # # if the word begins with "oo" replace it with "#w"
    # if word[:2] == "oo":
    #     word = "#w" + word[2:]
        
    # if the word ends with "'" replace it with "}"
    if word[-1:] == "'":
        word = word[:-1] + "}"
        
    # HAMZA IN THE MIDDLE OF THE WORD
    # if we find a "i'" or "'i" or "ī'" or "y'" or "ȳ'" replace it with "{"
    cond = "i'" in word or "'i" in word or "ī'" in word or "y'" in word or "ȳ'" in word
    if cond:
        word = word.replace("i'", "{")
        word = word.replace("'i", "{")
        word = word.replace("ī'", "{")
        word = word.replace("y'", "{")
        word = word.replace("ȳ'", "{")
    # else if we find a "o'" or "'o" replace it with "&"
    elif "o'" in word or "'o" in word:
        word = word.replace("o'", "&")
        word = word.replace("'o", "&")
    # else if we find a "ä'" or "w'" or "w̄'"  or "ō'" replace it with "}"
    elif "ä'" in word or "w'" in word or "w̄'" in word or "ō'" in word:
        word = word.replace("ä'", "}")
        word = word.replace("w'", "}")
        word = word.replace("w̄'", "}")
        word = word.replace("ō'", "}")
    else:
        # replace all "'" with "#"
        word = word.replace("'", "#")
        
        
    # =================== LETTRES DOUBLES ===================
    
    # replace all "th" with "T"
    word = word.replace("th", "T")
    # replace all "t̄h" with "T̄"
    word = word.replace("t̄h", "T̄")
    
    # replace all "kh" with "ḳ"
    word = word.replace("kh", "ḳ")
    # replace all "k̄h" with "ḳ̄"
    word = word.replace("k̄h", "ḳ̄")
    
    # replace all "dh" with "ḏ"
    word = word.replace("dh", "ḏ")
    # replace all "d̄h" with "ḏ̄"
    word = word.replace("d̄h", "ḏ̄")
    
    # replace all "sh" with "ṡ"
    word = word.replace("sh", "ṡ")
    # replace all "s̄h" with "ṡ̄"
    word = word.replace("s̄h", "ṡ̄")

    # replace all "ḍh" with "Z"
    word = word.replace("ḍh", "Z")
    # replace all "ḍ̄h" with "Z̄"
    word = word.replace("ḍ̄h", "Z̄")
    
    # replace all "gh" with "ġ"
    word = word.replace("gh", "ġ")
    # replace all "ḡh" with "ġ̄"
    word = word.replace("ḡh", "ġ̄")
    
    
    # =================== SHADDA AT THE END OF THE WORD ===================
    # replace all "̄" with "~" in the case that the previous letter is not "a" or "o" or "i"
    if word[-1:] == "̄" and word[-2:-1] != "a" and word[-2:-1] != "o" and word[-2:-1] != "i":
        word = word[:-1] + "~"
    
    word = word.replace("̄", "~")
    
    # alif at the end of the word
    if word[-2:] == "ạ":
        # insert a "a" just before the "ạ"
        word = word[:-1] + "a" + word[-1:]
        
        
    # if we found a "k~"
    # if "k~" in word:
    #     print("k~ in word: ", word)
        
    # wa
    if word == "w>":
        word = "wa"
    
    
    
    # =================== WORDS WITH ARTICLE ===================
    # if we found a "-" in the word, split it
    if "-" in word:
        firstPart = word.split("-")[0]
        secondPart = word.split("-")[1]
        firstLetterOfFirstPart = firstPart[0]
        lastLetterOfFirstPart = firstPart[-1]
        firstLetterOfSecondPart = secondPart[0]
        # if the last letter of the first part equals to the first letter of the second part
        if lastLetterOfFirstPart == firstLetterOfSecondPart:
            # add a "~" after the first letter of the second part
            secondPart = secondPart[0] + "~" + secondPart[1:]
            if firstLetterOfFirstPart != "e":
                firstPart = firstLetterOfFirstPart + "æl"
            else :
                firstPart = "æl"
            return transliterate(firstPart) + transliterate(secondPart)
        else:
            if firstLetterOfFirstPart != "e":
                firstPart = firstLetterOfFirstPart + "æl"
            else :
                firstPart = "æl"
            return transliterate(firstPart) + transliterate(secondPart)

        

    return transString(word)

