# перевод из i-ой системы счисления в 10-чную
def into_ten():
    n = int(input("Из какой системы счисления конвертируем"))
    num = int(input("Введите число"))
    count = 0
    last_digit = 0
    while num != 0:
        last_digit += (num % 10) * n**count
        count += 1
        num //= 10
    print(last_digit)

# перевод из 10-чной в i-ую систему счисления
def from_ten():
    n = int(input('В какую систему конвертируем: '))
    num = int(input('Введите число: '))
    res_list = []
    while num != 0:
        x = num % n
        if x >= 10:
            sym = chr(87 + x)
            res_list.insert(0, str(sym.upper()))
        else:
            res_list.insert(0, str(x))
        num = num // n
    print(''.join(res_list))

# перевод из 10-чной во 2-чную, в 8-чную, в 16-чную с помощью встроенных функций
def into_ten_bulits():
    n = int(input())
    bin_num = bin(n)
    oct_num = oct(n)
    hex_num = hex(n)
    print(bin_num[2:])
    print(oct_num[2:])
    print(hex_num[2:].upper())

