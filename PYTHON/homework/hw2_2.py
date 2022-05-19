from datetime import datetime
current_time = datetime.now().time()
choice = input("""Введите время в формате "hh:mm", 
либо нажмите "Enter" для использования текущего времени:\n""")
a, b = map(int, choice.split(":"))

if not choice:
    H = current_time.hour
    M = current_time.minute
elif a < 24 and ":" in choice and b < 60 and len(choice) == 5:
    H, M = a, b
else:
    print("""Формат ввода времени не верен! (hh:mm)
    Использовано текущее время""")
    H = current_time.hour
    M = current_time.minute
    
dic_hour = {1: "один час", 2: "два часа", 3: "три часа", 4: "четыре часа", 5: "пять часов",
            6: "шесть часов", 7: "семь часов", 8: "восемь часов", 9: "девять часов",
            10: "десять часов", 11: "одиннадцать часов", 12: "двенадцать часов",
            13: "один час", 14: "два часа", 15: "три часа", 16: "четыре часа", 17: "пять часов", 
            18: "шесть часов", 19: "семь часов", 20: "восемь часов", 21: "девять часов",
            22: "десять часов", 23: "одиннадцать часов", 24: "двенадцать часов"}
dic_hour_2 = {1: "второго", 2: "третьего", 3: "четвертого", 4: "пятого", 5: "шестого",
              6: "седьмого", 7: "восемого", 8: "девятого", 9: "десятого", 10: "одиннадцатого",
              11: "двенадцатого", 12: "первого", 13: "второго", 14: "третьего", 15: "четвертого",
              16: "пятого", 17: "шестого", 18: "седьмого", 19: "восемого", 20: "девятого",
              21: "десятого", 22: "одиннадцатого", 23: "двенадцатого", 0: "первого"}
dict_hour_3 = {1: "час", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть",
               7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одиннадцать",
               12: "двенадцать", 13: "час", 14: "два", 15: "три", 16: "четыре", 17: "пять",
               18: "шесть", 19: "семь", 20: "восемь", 21: "девять", 22: "десять", 
               23: "одиннадцать", 24: "двенадцать"}
k = {0: "ровно", 1: "одна", 2: "две", 3: "три", 4: "четыре", 5: 'пять',
     6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
     10: 'десять', 11: 'одиннадцать', 12: "двенадцать",
     13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 
     16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать',
     19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
     40: 'сорок', 50: 'пятьдесят'}
k_2 = {1: "одной минуты", 2: "двух минут", 3: "трех минут", 4: "четырех минут", 5: 'пяти минут',
     6: 'шести минут', 7: 'семи минут', 8: 'восеми минут', 9: 'девяти минут',
     10: 'десяти минут', 11: 'одиннадцати минут', 12: "двенадцати минут",
     13: 'тринадцати минут', 14: 'четырнадцати минут', 15: 'пятнадцати минут'}
M1 = M % 10
M2 = M - M1
if M in k:
    y = k.get(M)
else:
    y = k.get(M2) + " " + k.get(M1)

if M == 0:
    print(dic_hour.get(H), y)
elif M < 30 or M > 30 and M < 45:
    print(y, "минут", dic_hour_2.get(H))
elif M == 30:
    print("половина", dic_hour_2.get(H))
elif M >= 45:
    print("без", k_2.get(60 - M), dict_hour_3.get(H))
else:
    print(dic_hour.get(H), y, "минуты")