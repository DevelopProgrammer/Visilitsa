from random import *
word_list = ["человек", "тетка", "мяч", "дерево", "земля", "круг", "диван", "книга", "файл", "компьютер"]

def get_word():
    return choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Давайте играть в угадайку слов")
    print(display_hangman(tries))
    print(word_completion)
    while True:
        guess = input("Введите букву: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"Вы уже вводили букву {guess}")
            elif guess not in word:
                print(f"Буквы {guess} нет в слове")
                tries -= 1
                if tries == 0:
                    print(f"Вы проиграли. Загаданное слово {word}")
                    break
                guessed_letters.append(guess)
            else:
                print(f"Молодец! Буква {guess} есть в слове")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                list2 = [i for i in range(len(word)) if word[i] == guess]
                for i in list2:
                    word_as_list[i] = guess
                word_completion = "".join(word_as_list)
                if not "_" in word_completion:
                    print("Поздравляем вы угадали слово")
                    print(word_completion)
                    print()
                    break

        else:
            print("Введите букву: ")
        print(display_hangman(tries))
        print(word_completion)
        print()


word = get_word()
play(word)

while True:
    s = input("Хочешь сыграть еще раз? (Ведите да/нет) ")
    if s == "да":
        word
        print(play(word))
    else:
        print("Будем ждать твоего возвращения")
        break


