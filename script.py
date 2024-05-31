from finalScript import transliterate

dictionnary = {
    1: "wāꜧid",
    2: "thnīn",
    3: "thlātha",
    # 3: "tlātha",
    4: "arbзa",
    5: "khamsa",
    6: "sit̄a",
    7: "sabзa",
    8: "thmānya",
    9: "tisзa",
    10: "зashra",
    11: "aꜧdāsh",
    12: "athnāsh",
    13: "thloṭāsh",
    14: "arbaзṭāsh",
    15: "khamsṭāsh",
    16: "sit̄āsh",
    17: "sbaзṭāsh",
    18: "thmonṭāsh",
    19: "tsaзṭāsh",
    20: "зishrīn",
    30: "thlāthīn",
    40: "arbзīn",
    50: "khamsīn",
    60: "sit̄īn",
    70: "sabзīn",
    80: "thmānīn",
    90: "tisзīn",
    100: "myā",
    200: "mītīn",
    300: "tlātha myā",
    1000: "alf",
    2000: "alfīn",
    3000: "tlātha ālāf",
    1000000: "malyōn",
    2000000: "zōz mlāyin",
    1000000000: "milyār",
    2000000000: "zōz milyārāt",
    "milles": "ālāf",
    "millions": "mlāyin",
    "milliards": "milyārāt"
}    

def convertTens(number):
    units = number % 10
    tens = number - units
    return dictionnary[units] + " w " + dictionnary[tens]

def convertHundreds(number):
    hundreds = number // 100
    tens = number - hundreds * 100
    if tens == 0:
        return dictionnary[hundreds] + " " + dictionnary[100]
    # else:
    if hundreds == 1:
        return dictionnary[100] + " w " + convert(tens)
    elif hundreds == 2:
        return dictionnary[200] + " w " + convert(tens)
    else:
        return dictionnary[hundreds] + " " + dictionnary[100] + " w " + convert(tens)

def convertThousands(number):
    thousands = number // 1000
    hundreds = number - thousands * 1000
    
    # print("Thousands: " + str(thousands) + " Hundreds: " + str(hundreds))
    
    # if hundreds == 0:
    #     return convert[thousands] + " " + dictionnary["milles"]
    
    if thousands == 1:
        if hundreds == 0:
            return dictionnary[thousands] + " " + dictionnary["milles"]
            # return dictionnary[thousands] + " " + dictionnary["milles"]
        return dictionnary[1000] + " w " + convert(hundreds)
    elif thousands == 2:
        if hundreds == 0:
            return dictionnary[thousands] + " " + dictionnary["milles"]
        return dictionnary[2000] + " w " + convert(hundreds)
    else:
        if hundreds == 0:
            return convert(thousands) + " " + dictionnary["milles"]
        return convert(thousands) + " " + dictionnary["milles"] + " w " + convert(hundreds)
    
    

def convertMillions(number):
    millions = number // 1000000
    thousands = number - millions * 1000000    
    if millions == 1:
        if thousands == 0:
            return dictionnary[1000000]
        return dictionnary[1000000] + " w " + convert(thousands)
    elif millions == 2:
        if thousands == 0:
            return dictionnary[2000000]
        return dictionnary[2000000] + " w " + convert(thousands)
    else:
        if thousands == 0:
            return convert(millions) + " " + dictionnary["millions"]
        return convert(millions) + " " + dictionnary["millions"] + " w " + convert(thousands)

def convertBillions(number):
    billions = number // 1000000000
    millions = number - billions * 1000000000
    if billions == 1:
        # if millions == 0:
        #     return dictionnary[1000000000]
        return dictionnary[1000000000] + " w " + convert(millions)
    elif billions == 2:
        # if millions == 0:
        #     return dictionnary[2000000000]
        return dictionnary[2000000000] + " w " + convert(millions)
    else:
        if millions == 0:
            return convert(billions) + " " + dictionnary["milliards"]
        return convert(billions) + " " + dictionnary["milliards"] + " w " + convert(millions)


def convert(number):
    if number in dictionnary:
        return dictionnary[number]
    
    if number < 100:
        return convertTens(number)
    elif number < 1000:
        return convertHundreds(number)
    elif number < 1000000:
        return convertThousands(number)
    elif number < 1000000000:
        return convertMillions(number)
    else:
        return convertBillions(number)
   
   
   
   
if __name__ == "__main__":
    numbers = [i for i in range(1, 1000)]
    result = {}
    for num in numbers:
        result[num] = [convert(num), transliterate(convert(num))]

    # add it to the file
    file = open("conversion.txt", "w", encoding="utf-8")
    for key, value in result.items():
        file.write(str(key) + " : " + str(value[0]) + " : " + str(value[1]) + "\n")
   
   
   
   
   
   
   
   
   
   
   
   
    


# file = open("conversion.txt", "w", encoding="utf-8")
# for i in range(1, 1000000000):
#     print(str(i) + " : " + str(convert(i)))
#     file.write(str(i) + " : " + str(convert(i)) + "\n")
    
# file.close()


# import threading

# def run_conversion(start, end):
#     file = open("conversion.txt", "a", encoding="utf-8")
#     for i in range(start, end):
#         print(str(i) + " : " + str(convert(i)))
#         file.write(str(i) + " : " + str(convert(i)) + "\n")
#     file.close()

# threads = []
# for i in range(10):
#     start = i * 100000000 // 10 + 1
#     end = (i + 1) * 100000000 // 10
#     thread = threading.Thread(target=run_conversion, args=(start, end))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()
