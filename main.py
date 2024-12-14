import json
cars_kol=5
count=0
with open("cars.json", 'r', encoding='utf-8') as file:
 inf = json.load(file)
commands = [
    "Вывести все записи",
    "Вывести запись по полю",
    "Добавить запись",
    "Удалить запись по полю",
    "Выйти из программы"
]
actions_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
}
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
    count += 1
    actions_count[1] += 1
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
     count += 1
     actions_count[2] += 1
  elif num==3:
     proverka=False
     new_id=cars_kol+1  
     new_name = input("Введите название модели: ")
     new_manufacturer = input("Введите производителя: ")
     new_is_petrol = input("Машина заправляется бензином (да/нет): ").lower()
     if new_is_petrol!="да" or new_is_petrol!="нет":
        while proverka==False:
           new_is_petrol_1 = input("Неккоректное значение ,машина заправляется бензином? (да/нет): ").lower()
           if new_is_petrol_1=="да" or new_is_petrol_1=="нет":
            new_is_petrol = new_is_petrol_1
            proverka == True
     new_tank_volume = input("Введите объём бака: ")
     while not new_tank_volume.isdigit():
      print("Неверное значение,введите ответ корректно")
      new_tank_volume = input("Введите объём бака: ")
     new_tank_volume = float(new_tank_volume)
     if new_is_petrol == "да":
       petrol_proverka = True
     else: 
      petrol_proverka=False 
     new_car = {
      "id": new_id, 
      "name": new_name,
      "manufacturer": new_manufacturer,
      "is_petrol": petrol_proverka,
      "tank_volume": new_tank_volume
       }
     inf.append(new_car)
     with open("cars.json",'w', encoding='utf-8') as other_file:
      json.dump(inf,other_file)
     print("Машина добавлена!")
     count += 1
     actions_count[3]+= 1
  elif num==4:
    id = input("Введите номер записи машины: ")
    while not id.isdigit():
      id=input("Некорректное  значение.Введите номер записи машины снова: ")
    id=int(id)
    for car in inf:
      if id ==car.get("id"):
        inf.remove(car)
        proverka=True
        break
    if not proverka:
      print("Машина не найдена ")
    with open("cars.json",'w', encoding='utf-8') as other_file:
      json.dump(inf,other_file)
    print("Машина удалена")
    count+=1
    actions_count[4] += 1
  elif num==5:
    actions_count[5] += 1
    print(f"""
          Программа завершена.Количество всех операций: {count}
           """)
    for el in commands :
      for i in actions_count:
       print(f"""{el}:{i} """)
    
