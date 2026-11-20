import string
print('Введите пароль:')
password = input()
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
if len(password) != 8:
    print("Длина пароля не равна 8")
if not any(symbol.isupper() for symbol in password):
    print("В пароле отсутствуют заглавные буквы")
if not any(symbol.islower() for symbol in password):
    print("В пароле отсутствуют строчные буквы")
if not any(symbol.isdigit() for symbol in password):
    print("В пароле отсутствуют цифры")
if not any(symbol in '*-#' for symbol in password):
    print("В пароле отсутствуют специальные символы")
if not all(symbol in allowed for symbol in password):
    print("В пароле используются непредусмотренные символы")
if (len(password) == 8 and
    any(symbol.isupper() for symbol in password) and
    any(symbol.islower() for symbol in password) and
    any(symbol.isdigit() for symbol in password) and
    any(symbol in '*-#' for symbol in password) and
    all(symbol in allowed for symbol in password)):
    print("Надежный пароль")