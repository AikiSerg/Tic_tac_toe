# Tic_tac_toe Игра крестики нолики

# Словарь - координаты полей, координаты поля в виде кортежа(их не надо изменять, быстрее будет выполняться программа)
dict_coordinates = {
                    "coor_y" : "    ""0""  ""1""  ""2",
                    "coor_x_0" : "0",
                    "00" : "-",
                    "01" : "-",
                    "02" : "-",
                    "coor_x_1" : "1",
                    "10": "-",
                    "11": "-",
                    "12": "-",
                    "coor_x_2" : "2",
                    "20": "-",
                    "21": "-",
                    "22": "-",
                    }

# Графическая оболочка игры крестики нолики

def wrapper():
    print(
      f"{dict_coordinates['coor_y']}\n"
      f" {dict_coordinates['coor_x_0']}  {dict_coordinates['00']}  {dict_coordinates['01']}  {dict_coordinates['02']}\n"
      f" {dict_coordinates['coor_x_1']}  {dict_coordinates['10']}  {dict_coordinates['11']}  {dict_coordinates['12']}\n"
      f" {dict_coordinates['coor_x_2']}  {dict_coordinates['20']}  {dict_coordinates['21']}  {dict_coordinates['22']}\n")



# Условиями победы!
Winner = "УРААААА! ПОБЕДА!"
def dict_coordinates_winner_1():
    if dict_coordinates['00'] == dict_coordinates['01'] == dict_coordinates['02'] != "-":
        print(Winner)
    elif dict_coordinates['10'] == dict_coordinates['11'] == dict_coordinates['12'] != "-":
        print(Winner)
    elif dict_coordinates['20'] == dict_coordinates['21'] == dict_coordinates['22'] != "-":
        print(Winner)
    elif dict_coordinates['00'] == dict_coordinates['11'] == dict_coordinates['22'] != "-":
        print(Winner)
    elif dict_coordinates['20'] == dict_coordinates['11'] == dict_coordinates['02'] != "-":
        print(Winner)
    else:
        return


# Функция проверки выеденных чисел со словарем, если верно, изменение словаря

def data_comparisson_play_1():
    # вводим по оси Х и У
    axis_x = str(input("Введите координату(цифру) по оси Х и нажмите ENTER:"))
    print(axis_x)
    axis_y = str(input("Введите координату(цифру) по оси У и нажмите ENTER:"))
    print(axis_y)
    print(f"Вы ввели координату: --- {axis_x}{axis_y} ---")
    # Вводим крестик или нолик
    axis_X_O = str(input("Введите крестик(X) или нолик(0) и нажмите ENTER:"))
    print(f"Вы ввели: --- {axis_X_O} ---")
    coordinate_c = axis_x + axis_y
    #print(coordinate_c)
    #print(type(coordinate_c))
    X_O = axis_X_O
    for k in dict_coordinates.copy():
    #print("Из функции", k)
        if coordinate_c == k:
        #print("Ок")
            dict_coordinates[k] = X_O # Меням - в словаре на Х или 0
            return dict_coordinates
        #else:
            #print("Повтор")

    else:
        print("Вы ввели неправильное число")

# Начинаем игру!
wrapper()
print(f"ОСЬ Х горизонтальная (->)\n"
         f"ОСЬ У вертикальная (|)\n"
      )

print("Поехали!")
# Ход 1
data_comparisson_play_1()
wrapper()
dict_coordinates_winner_1()
# Ход 2
data_comparisson_play_1()
wrapper()
dict_coordinates_winner_1()
# Ход 3
data_comparisson_play_1()
wrapper()
dict_coordinates_winner_1()
# Ход 4
data_comparisson_play_1()
wrapper()
dict_coordinates_winner_1()
# Ход 5
data_comparisson_play_1()
wrapper()
dict_coordinates_winner_1()
# Ход 6
data_comparisson_play_1()
wrapper()
dict_coordinates_winner_1()
# Ход 7
data_comparisson_play_1()
wrapper()
dict_coordinates_winner_1()
# Ход 8
data_comparisson_play_1()
wrapper()
dict_coordinates_winner_1()
# Ход 9
data_comparisson_play_1()
wrapper()
dict_coordinates_winner_1()