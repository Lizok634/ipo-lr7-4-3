import json#подключаем библиотеку
count=0
with open("cars.json", 'r', encoding = 'utf-8') as file:#открываем файл cars.json и говорим, что будем читать из файла
    inf = json.load(file) #Присваеваем переменной inf 
def validation(prompt):#создаем функцию для проверки введенной информации на число
     while(True):
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else: 
            print("Это не число")
    
def all_commands():#создаем функцию для вывода всех комманд
    commands="""
    1.Вывести все записи
    2.Вывести запись по полю
    3.Добавить запись
    4.Удалить запись по полю
    5.Выйти из программы"""
    print(commands)
def all_cars():#создаем функцию для вывода информации о всех машинах
    global count #глобальная переменная
    for car in inf:
         print(f"""
             Номер записи: {car["id"]},
             Название модели: {car["name"]},
             Название производителя: {car["manufacturer"]},
             Заправляется бензином: {car["is_petrol"]},
             Объем бака: {car["tank_volume"]}
              """)
    count+=1

def one_car():#создаем функцию для вывода одной машины
    global count
    proverka=False
    id=input("Введите номер записи машины: ")
    while not id.isdigit():#проверка на число
        print("Неккоректное значение. Попробуйте еще раз :)")
        id = input("Введите номер записи машины : ")
    for car in inf:
        if id == car.get("id"):
            print(f"""
            Номер записи: {car["id"]},
            Название модели: {car["name"]},
            Название производителя: {car["manufacturer"]},
            Заправляется бензином: {car["is_petrol"]},
            Объем бака: {car["tank_volume"]}
            """)
            proverka=True
            count+=1
            break
    if proverka==False:
        print("Запись не найдена")
def new_car():#создаем функцию для добавления новой машины
    global count
    proverka=False
    new_id=len(inf) + 1 
    new_name = input("Введите название модели: ")
    new_manufacturer = input("Введите производителя: ")
    new_is_petrol = input("Машина заправляется бензином (да/нет): ").lower()
    if new_is_petrol!="да" and new_is_petrol!="нет":#проверяем является ли введенное значение корректным
        while proverka == False:
            new_is_petrol_1 = input("Неккоректное значение ,машина заправляется бензином? (да/нет): ").lower()
            if new_is_petrol_1=="да" or new_is_petrol_1=="нет":
                new_is_petrol = new_is_petrol_1
                proverka = True
    if new_is_petrol == "да":
            petrol_proverka = True
    else: 
        petrol_proverka=False 
    new_tank_volume=validation("Введите объем бака: ")
    new_car = {
    "id": new_id, 
    "name": new_name,
    "manufacturer": new_manufacturer,
    "is_petrol": petrol_proverka,
    "tank_volume": new_tank_volume
    }
    inf.append(new_car)#добавляем новую машину
    with open("cars.json",'w', encoding='utf-8') as other_file:
        json.dump(inf,other_file)
    print("Машина добавлена!")
    count+=1
def del_car():#создаем функцию для удаления машины
    global count
    proverka=False
    id=input("Введите номер записи машины: ")
    while not id.isdigit():
        print("Неккоректное значение. Попробуйте еще раз :)")
        id = input("Введите номер записи машины : ")
    id=int(id)
    for car in inf:
         if id ==car.get("id"):
            inf.remove(car)#удаляем машину
            proverka=True
            break
    if not proverka:
        print("Машина не найдена ")
    else:
        with open("cars.json",'w', encoding='utf-8') as other_file:
            json.dump(inf,other_file)
            print("Машина удалена")
    count+=1
def prog_exit():#создаем функцию для выхода из программы
    global count
    count+=1
    print(f"Работа завершена :{count}")

while True:
        all_commands()
        num = validation("Ваше значение: ")
        if num==1:
            all_cars()
        elif num==2:
            one_car()
        elif num==3:
             new_car()
        elif num==4:
            del_car()
        elif num==5:
            prog_exit()
        else:
            print("Веденного номера не существует")
