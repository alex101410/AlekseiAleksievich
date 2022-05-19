choice = input("""Введите время в формате "hh:mm", 
либо нажмите "Enter" для использования текущего времени:\n""")
if choice.replace(":","").isdigit():
    print("OK")
else:
    print("BAD")