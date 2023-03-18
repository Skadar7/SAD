from pprint import pprint


def pareto(i, arr):
    res = [0, 0]
    answer = []
    for x in range(i+1, len(arr)):
        if arr[i][1] <= arr[x][1]:
            res[0] += 1
        else:
            res[1] += 1

        if arr[i][2] <= arr[x][2]:
            res[0] += 1
        else:
            res[1] += 1

        if arr[i][3] >= arr[x][3]:
            res[0] += 1
        else:
            res[1] += 1

        if arr[i][4] >= arr[x][4]:
            res[0] += 1
        else:
            res[1] += 1

        if arr[i][5] <= arr[x][5]:
            res[0] += 1
        else:
            res[1] += 1

        if res[0] == 5:
            answer.append(arr[i])
        elif res[1] == 5:
            answer.append(arr[x])

        res = [0, 0]

    return answer

def lex(arr):
    borders_max = {}
    borders_min = {}
    for i in range(len(arr[0]) - 1):
        temp = []
        for j in range(len(arr)):
            temp.append(arr[j][i + 1])
        borders_max[i + 1] = max(temp)
        borders_min[i + 1] = min(temp)
    while True:
        print("[1] - Цена\n[2] - Площадь\n[3] - Удаленность от метро\n"
              "[4] - Рейтинг\n[5] - Состояние квартиры\n[6] - Закончить")
        choice = int(input())
        if choice == 3 or choice == 4:
            arr = list(filter(lambda x: x[choice] == borders_max[choice], arr))
        else:
            arr = list(filter(lambda x: x[choice] == borders_min[choice], arr))
        if len(arr) < 2:
            return arr

def main_crit(arr):
    bord = ["Цена", "Площадь", "Удаленность от метро", "Рейтинг", "Состояние квартиры"]
    borders_max = {}
    borders_min = {}
    for i in range(len(arr[0]) - 1):
        temp = []
        for j in range(len(arr)):
            temp.append(arr[j][i + 1])
        borders_max[i + 1] = max(temp)
        borders_min[i + 1] = min(temp)

    print("[1] - Цена\n[2] - Площадь\n[3] - Удаленность от метро\n"
          "[4] - Рейтинг\n[5] - Состояние квартиры\n[6] - Закончить")
    choice = int(input())
    print("Установите нижние границы для всех остальных критериев")
    for i in range(len(bord)):
        if i+1 == choice:
            continue
        print("Нижняя граница для {}: ".format(bord[i]))
        ent = float(input())
        if ent > borders_max[i+1]:
            print("Желаемая граница больше максимального, попробуйте еще раз")
            continue
        arr = list(filter(lambda x: x[i+1] > ent, arr))
    if len(arr) == 1:
        return arr
    else:
        if choice == 2 or choice == 5:
            arr = list(filter(lambda x: x[choice] == borders_max[choice], arr))
        else:
            arr = list(filter(lambda x: x[choice] == borders_min[choice], arr))
        return arr

def narrowing(arr):
    borders_max = {}
    borders_min = {}
    for i in range(len(arr[0])-1):
        temp = []
        for j in range(len(arr)):
            temp.append(arr[j][i+1])
        borders_max[i+1] = max(temp)
        borders_min[i+1] = min(temp)

    print("Применим сужение к полученной таблице, установим верхние и/или нижние границы")
    print("[1] - Цена\n[2] - Площадь\n[3] - Удаленность от метро\n"
          "[4] - Рейтинг\n[5] - Состояние квартиры\n[6] - Закончить")
    choice = int(input())

    while choice != 6:
        print("Установить верхние границы - 1, нижние - 0")
        bord = int(input())
        print("Введите границу: ")
        ent = int(input())
        if bord == 1:
            if ent < borders_min[choice]:
                print("Желаемая граница меньше минимальной, попробуйте еще раз")
                continue
            arr = list(filter(lambda x: x[choice] <= ent, arr))
        elif bord == 0:
            if ent > borders_max[choice]:
                print("Желаемая граница больше максимальной, попробуйте еще раз")
                continue
            arr = list(filter(lambda x: x[choice] >= ent, arr))
        print("[1] - Цена\n[2] - Площадь\n[3] - Удаленность от метро\n"
              "[4] - Рейтинг\n[5] - Состояние квартиры\n[6] - Закончить")
        choice = int(input())
    return arr

if __name__ == '__main__':

    arr = [["Эсенево", 8, 105, 4, 7.1, 9.1], ["Медведкого", 8.7, 55, 1.2, 6.9, 6.2],
           ["Солнцево", 7.1, 43, 1.6, 5.2, 4.4], ["Марьино", 5.2, 26, 2.0, 3.2, 3.1],
           ["Новопеределкино", 8.7, 57, 2.2, 6.9, 6.3], ["Ростокино", 10.6, 53, 1.0, 6.8, 6.6],
           ["ВДНХ", 3.1, 55, 1.2, 6.9, 6.2], ["Раменки", 3.2, 28, 3.7, 2.2, 2.1],
           ["Савёловская", 11.6, 67, 0.8, 6.9, 6.9], ["Мичуринский проспект", 12.1, 60, 0.7, 7.0, 7.0]]

    answ = []
    for i in range(len(arr)):
        answ += pareto(i, arr)

    print(answ)
    #pprint(narrowing(answ))
    #pprint(main_crit(answ))
    #pprint(lex(answ))


