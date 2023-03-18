def person(name, age):
    def get(obj):
        match obj:
            case 'name':
                return name
            case 'age':
                return age
    return get

def replace(p, obj, change):
    match obj:
        case 'name':
            return person(change, p('age'))
        case 'age':
            return person(p('name'), change)

def get(p, atr):
    return p(atr)

p1 = person(name='Иван', age=20)
p2 = replace(replace(p1, 'name', 'Алексей'), 'age', 21)
print(get(p1, 'name'), get(p1, 'age'))
print(get(p2, 'name'), get(p2, 'age'))