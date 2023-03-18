def pair(val, tail):
    def get(obj):
        match obj:
            case 'val':
                return val
            case 'tail':
                return tail
    return get


def first(lst):
    return lst('val')# (возвращает значение головы списка)


def rest(lst):
    while lst('tail'): lst = lst('tail')
    return lst('val') # (возвращает хвост списка).


def make_list(*args):
    lst = None
    for i in args[::-1]:
        lst = pair(i, lst)
    return lst


def list_to_string(lst):
    s = ''
    while lst('tail'):
        s += str(lst('val'))
        lst = lst('tail')
    return s # возвращающую строку, содержащую элементы списка.


def list_range(low, high):
    lst = None
    for i in range(high, low - 1, -1):
        lst = pair(i, lst)
    return lst # возвращающую список чисел от low до high включительно.


def foldl(func, lst, acc):
    res = acc
    while lst:
        res = func(res, lst)
        lst = lst('tail')# вычисляющую свертку элементов списка, аналогично reduce.
    return res


def list_sum(lst):
    def summ(a, b):
        return a + b('val')
    return foldl(summ, lst, 0)# для вычисления суммы элементов списка с помощью foldl.


def fact(n):
    def mult(a, b):
        return a * b('val')
    return foldl(mult, list_range(1, n), 1)# для вычисления факториала с помощью foldl и list_range.


def list_to_py(lst):
    def to_py(a, b):
        a.append(b('val'))
        return a
    return foldl(to_py, lst, [])# для преобразования списка в обычный список Питона с помощью foldl.


def list_reverse(lst):
    def rev(a, b):
        return pair(b('val'), a)
    return foldl(rev, lst, None)# для разворота списка в обратном направлении с помощью foldl.

def foldr(func, lst, acc):
    lst = list_reverse(lst)
    res = acc
    while lst:
        res = func(res, lst)
        lst = lst('tail')
    return res# вычисляющую свертку справа для элементов списка.


def list_map(func, lst):
    def m(a, b):
        return pair(func(b('val')), a)
    return foldr(m, lst, None)# аналог map


def list_filter(pred, lst):
    def comp(a, b):
        return pair(b('val'), a) if pred(b('val')) else a
    return foldr(comp, lst, None)# аналог filter


def sum_odd_squares(lst):
    return list_sum(list_map(lambda x: x**2, list_filter(lambda x: x % 2 , lst)))
# для вычисления суммы квадратов нечетных чисел списка с помощью list_sum, list_map и list_filter.


def list_replace(lst, index, value):
    res = None
    i = 0
    while lst:
        res = pair(lst('val'), res) if i != index else pair(value, res)
        lst = lst('tail')
        i += 1
    return list_reverse(res) # для изменения элемента списка по индексу.



print(list_to_py(list_replace(list_range(0,5), 3, 0)))
print(fact(6))