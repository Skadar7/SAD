import codecs
import string as str
import matplotlib.pyplot as plt


file = codecs.open( "dates.txt", "r", "utf-8" )
data = file.read()
file.close()
games_for_years = [0] * 28

n = 1981
years_list = [0] * 28
for i in range(28):
    years_list[i] = n
    n += 1
years = tuple(years_list)

def get_games_for_years(data):
    for i in range(5261):
        year = data.split('\n')[i].split(';')[3].split('"')[1]
        if year.isdigit():
            n = int(year) - 1981
            games_for_years[n] += 1
    return games_for_years

def give_first():
    games_for_years_list = get_games_for_years(data)
    games_for_years = tuple(games_for_years_list)

    plt.plot(years, games_for_years)
    plt.show()

give_first()
dict_data = {}
temp = []

for line in data.split("\n"):
    words = line.split(";")
    year = words[3].split('"')[1]
    genre = words[1].split('"')[1]
    if year.isdigit():
        if year not in dict_data.keys():
            dict_data[year] = {}
        if genre not in dict_data[year].keys():
            dict_data[year][genre] = 0
        dict_data[year][genre] += 1
        temp.append(genre)

keys = []
#удаление всех повторных элементов
for i in temp:
    if i not in keys:
        keys.append(i)

colon_width = 1
colon_space = 5
offset = 0 #сдвиг гистограмм нового жанра
for genge in keys:
    x_raw_list = range(offset, len(dict_data) * (len(keys)*colon_width + colon_space), len(keys) * colon_width + colon_space)
    x_list = [int(list(dict_data.keys())[x_raw_list.index(i)]) + (i % (len(keys) * colon_width + colon_space)) / 20 for i in x_raw_list]
    y_list = [(year[genge] if genge in year.keys() else 0) for year in dict_data.values()]
    offset += colon_width
    plt.bar(x_list, y_list, width = colon_width / 20, label = genge)
plt.legend()
plt.show()
