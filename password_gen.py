import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^'
chars = ''
password_count =  int(input('Введите количесво паролей для генерации '))
password_lenght = int(input('Введите длину одного парля '))
add_digits = (input("Включать ли цифры 0123456789? (д /н ) "))
add_lowercase_letters = input(('Включать буквы нижнего регистра abcdefghijklmnopqrstuvwxyz ?  ( д / н) ' ))
add_uppercase_letters = input(('Включать буквы верхнего регистра ABCDEFGHIJKLMNOPQRSTUVWXYZ ? ( д / н) '))
add_punctuation  = input(('Включать знаки пунктуации !#$%&*+-=?@^ ? (д / н) '))
add_incorrect_chars = input(('Исключать ли неоднозначные символы il1Lo0O ?  (д/ н) '))



if add_digits == 'д': 
    chars += '0123456789'
if add_lowercase_letters == 'д':
    chars += 'abcdefghijklmnopqrstuvwxyz'
if add_uppercase_letters  == 'д':
    chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if add_punctuation  == 'д':
    chars += '!#$%&*+-=?@^'
if add_incorrect_chars == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
         


def generate_password(password_lenght, chars):
    password = ''
    for j in range(password_lenght):
        password += random.choice(chars)
    return password

my_passwords = []
for _ in range(password_count):
    my_passwords.append(generate_password(password_lenght,chars))
for password in my_passwords:
    print(password)

finally_question = input(("Перед тем как ответить на вопрос сохраните сгенерированные пароли!!! Вам удобно исползование генератора паролей (д\н)? "))









    
    

    

