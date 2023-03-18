def Num(val):
    def get(obj):
        match obj:
            case 'oper':
                return str(val)
            case 'stack':
                return f'PUSH {val}'
            case 'val':
                return val
    return get


def Add(*items):
    def get(obj):
        match obj:
            case 'oper':
                return f"({' + '.join([i('oper') for i in items])})"
            case 'val':
                value = 0
                for i in items: value += i('val')
                return value
            case 'stack':
                return "{}\nADD".format('\n'.join([i('stack') for i in items]))
    return get


def Div(*items):
    def get(obj):
        match obj:
            case 'oper':
                return f"({' / '.join([i('oper') for i in items])})"
            case 'val':
                value = items[0]('val')
                for i in items[1:]: value /= i('val')
                return value
            case 'stack':
                return "{}\nDIV".format('\n'.join([i('stack') for i in items]))
    return get


def Mul(*items):
    def get(obj):
        match obj:
            case 'oper':
                return f"({' * '.join([i('oper') for i in items])})"
            case 'val':
                value = 1
                for i in items: value *= i('val')
                return value
            case 'stack':
                return "{}\nMUL".format('\n'.join([i('stack') for i in items]))
    return get


def Sub(*items):
    def get(obj):
        match obj:
            case 'oper':
                return f"({' - '.join([i('oper') for i in items])})"
            case 'val':
                value = items[0]('val')
                for i in items[1:]: value -= i('val')
                return value
            case 'stack':
                return "{}\nSUB".format('\n'.join([i('stack') for i in items]))
    return get


def PrintVisitor():
    def visit(obj):
        return obj('oper')
    return visit


def CalcVisitor():
    def visit(obj):
        return obj('val')
    return visit


def StackVisitor():
    def visit(obj):
        return obj('stack')
    return visit


ast = Add(Num(7), Div(Mul(Num(3), Num(2)), Num(10)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv(ast))
print(cv(ast))
print(sv(ast))