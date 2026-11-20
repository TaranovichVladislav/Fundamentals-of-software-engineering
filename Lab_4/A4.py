def IsValidNumber(cardNumber):
    return cardNumber.isdigit() and len(cardNumber) in [13, 15, 16]
def getCheckSum(cardNumber):
    checkSum = 0
    card = cardNumber[::-1]
    for i in range(len(card)):
        digit = int(card[i])
        if i % 2 == 1:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        checkSum = checkSum + digit
    return checkSum
def isValidCheckSum(checkSum):
    return checkSum % 10 == 0
def getCardType(cardNumber):
    if cardNumber.startswith("4") and len(cardNumber) in [13, 16]:
        return "Visa"
    elif len(cardNumber) == 15 and (cardNumber.startswith("34") or cardNumber.startswith("37")):
        return "American Express"
    elif len(cardNumber) == 16 and int(cardNumber[:2]) >= 51 and int(cardNumber[:2]) <= 55:
        return "MasterCard"
    else:
        return "Invalid"
cardNumber = input("Введите номер карты: ")
if IsValidNumber(cardNumber):
    if isValidCheckSum(getCheckSum(cardNumber)):
        print("Valid")
        print(getCardType(cardNumber))
    else:
        print("Invalid")
else:
    print("Неправильный ввод!")