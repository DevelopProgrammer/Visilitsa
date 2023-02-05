def change_str(sentence):
    for i in range(len(sentence)):
        sentence[i] = int(sentence[i])
    return sentence

def is_palindrom(password):
    first_digit = password.split(":")
    change_str(first_digit)
    a = str(first_digit[0])
    if a[:] == a[::-1]:
        return True
    else:
        return False

def is_have_two_digit(password):
    second_digit = password.split(":")
    change_str(second_digit)
    flag = True
    for i in range(2, second_digit[1]):
        if second_digit[1] % i == 0:
            flag = False
    if second_digit[1] == 1:
        return False
    elif flag == True:
        return True
    else:
        return False

def is_even_one(password):
    third_digit = password.split(":")
    change_str(third_digit)
    if third_digit[2] % 2 == 0:
        return True
    else:
        return False

def is_accept_length(password):
    length = password.split(":")
    if len(length) == 3:
        return True
    else:
        return False

def is_valid_password(password):
    if is_palindrom(password) == True and is_have_two_digit(password) == True and is_even_one(password) == True and is_even_one(password) == True:
        return True
    else:
        return False

psw = input()

print(is_accept_length(psw))
