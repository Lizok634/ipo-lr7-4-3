import json
count=5
with open("cars.json", 'r', encoding='utf-8') as file:
 inf = json.load(file)
commands = [
    "Вывести все записи",
    "Вывести запись по полю",
    "Добавить запись",
    "Удалить запись по полю",
    "Выйти из программы"
]
while True:
  print ("""
    1.Вывести все записи
    2.Вывести запись по полю
    3.Добавить запись
    4.Удалить запись по полю
    5.Выйти из программы""" )
  num=int(input("Ваше значение: "))
  if num==1:
    for car in inf:
      if car["is_petrol"] == True:
        pet="да"
      else:
        pet="нет"
      print(f"""
      Номер записи: {car["id"]},
      Название модели: {car["name"]},
      Название производителя: {car["manufacturer"]},
      Заправляется бензином: {pet},
      Объем бака: {car["tank_volume"]}
      """)
  elif num==2:
     id=input("Введите номер записи машины: ")
     while not id.isdigit():
        print("Неккоректное значение. Попробуйте еще раз :)")
        id = input("Введите номер записи машины : ")
     for car in inf:
        if id == car.get("id"):
          if car["is_petrol"] == True:
               pet="да"
          else:
               pet="нет"
          print(f"""
          Номер записи: {car["id"]},
          Название модели: {car["name"]},
          Название производителя: {car["manufacturer"]},
          Заправляется бензином: {pet},
          Объем бака: {car["tank_volume"]}
          """)
          break
        else:
          print("Запись не найдена")
  elif num==3:
     proverka=False
     new_id=count+1
     new_name = input("Введите название модели: ")
     new_manufacturer = input("Введите производителя: ")
     new_is_petrol = input("Машина заправляется бензином (да/нет): ").lower()
     if new_is_petrol=="да" or new_is_petrol=="нет":
      new_is_petrol = new_is_petrol.lower().strip()
     else:
        while proverka==False:
           new_is_petrol = input("Машина заправляется бензином (да/нет): ").lower()
           if new_is_petrol=="да" or new_is_petrol=="нет":
            new_is_petrol = new_is_petrol.lower().strip()
            proverka==True
    

 
