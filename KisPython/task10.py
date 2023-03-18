from pprint import pprint


def transpose(table):
    response = []
    for i in range(len(table[0])):
        response.append([])
        for j in range(len(table)):
            response[i].append(table[j][i])
    return response


def delete_empty_rows(table):
    return [row for row in table if row[0] is not None]


def delete_duplicate_rows(table):
    added = set()
    new_arr = []
    for i in table:
        if i[1] not in added:
            new_arr.append(i)
            added.add(i[1])
    return new_arr


def transformer(i, value):
    if i == 0:
        return "Выполнено" if value == '1' else "Не выполнено"
    if i == 3:
        replaced = value.replace('+7', '')
        return replaced[0:5] + " " + replaced[5:]


def transform(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if i == 2:
                continue
            if i == 1:
                nt = table[i][j].split("&")
                table[i][j] = nt[1].replace('@', '[at]')
                table[i+1][j] = "%.4f" % float(nt[0])
            else:
                table[i][j] = transformer(i, table[i][j])
    return table


def main(table):
    return transform(
        transpose(
            delete_duplicate_rows(
                delete_empty_rows(table))
            )
        )


if __name__ == "__main__":
    pprint(main([['0', '0.5&vanukev58@mail.ru', '0', '+7(383)519-07-93'],
                ['0', '0.4&lorberg91@mail.ru', '0', '+7(750)715-50-78'],
                ['1', '0.8&samomanz67@rambler.ru', '1', '+7(978)710-52-97'],
                ['1', '0.1&zimifev36@rambler.ru', '1', '+7(558)309-64-82'],
                [None, None, None, None],
                 [None, None, None, None],
                ['1', '0.1&zimifev36@rambler.ru', '1', '+7(558)309-64-82'],
                ['1', '0.1&zimifev36@rambler.ru', '1', '+7(558)309-64-82']]))
