#1-ый способ (декодирование рус. алфавит)
def decode_ru_sentence(shift):
    s = input("Введите сообшение: ")
    result = ''
    for i in s:
        if i.islower():
            k = ord(i) - shift
            if k < 1072:
                k += 32
            result += chr(k)
        elif i.isupper():
            k = ord(i) - shift
            if k < 1040:
                k += 32
            result += chr(k)
        else:
            result += i
    print(result)

#2-ой способ (декодирование англ. алфавит)
def decode_en_sentence(shift):
    s = input("Введите закодированное сообщение: ")
    result = ''
    for i in s:
        if i.islower():
            k = ord(i) - shift
            if k < 97:
                k += 26
            result += chr(k)
        elif i.isupper():
            k = ord(i) - shift
            if k < 65:
                k += 26
            result += chr(k)
        else:
            result += i
    print(result)

# 3-ий способ (шифрование рус. алфавит)
def code_ru_sentence(shift):
    s = input("Введите сообшение: ")
    result = ""
    for i in s:
        if i.islower():
            k = ord(i) + shift
            if k > 1103:
                k -= 32
            result += chr(k)
        elif i.isupper():
            k = ord(i) + shift
            if k > 1071:
                k -= 32
            result += chr(k)
        else:
            result += i
    print(result)

# 4-ый способ (шифрование англ. алфавит)
def code_en_sentence(shift):
    s = input("Введите сообшение: ")
    result = ""
    for i in s:
        if i.islower():
            k = ord(i) + shift
            if k > 122:
                k -= 26
            result += chr(k)
        elif i.isupper():
            k = ord(i) + shift
            if k > 90:
                k -= 26
            result += chr(k)
        else:
            result += i
    print(result)

def cesar_sentence(language, cesar_code):
    if language == "русский" and cesar_code == "шифр":
        code_ru_sentence(shift)
    elif language == "русский" and cesar_code == "дешифр":
        decode_ru_sentence(shift)
    elif language == "английский" and cesar_code == "шифр":
        code_en_sentence(shift)
    else:
        language == "английский" and cesar_code == "дешифр"
        decode_en_sentence(shift)


language = input("Выберите язык ru/en (введите русский/английский): ")
cesar_code = input("Выберите - шифрование/дешифрование (введите шифр/дешифр): ")
shift = int(input("Введите шаг сдвига: "))

cesar_sentence(language, cesar_code)


# 5-ый способ (шифрование англ. алфавит (каждое слово строки следует зашифровать с помощью циклического сдвига на длину этого слова)
#s = input().split()
#list1 = []
#for i in s:
 #   b = 0
  #  for k in range(len(i)):
   #     if not i[k].isalpha():
    #       b += 1
    #a = len(i)
    #result = ""
   # for j in range(len(i)):
    #    if i[j].islower():
     #       k = ord(i[j]) + a - b
      #      if k > 122:
       #         k -= 26
        #    result += chr(k)
        #elif i[j].isupper():
         #   k = ord(i[j]) + a - b
          #  if k > 90:
           #     k -= 26
            #result += chr(k)
        #else:
         #   result += i[j]
    #list1.append(result)


#print(*list1)

