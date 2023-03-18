from struct import *


FMT = dict(
    char='c',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def parse_a(buf, offs):
    a1 = []
    for _ in range(3):
        val, offs = parse_b(buf, offs)
        a1.append(val)
    a2, offs = parse_c(buf, offs)
    a3, offs = parse_d(buf, offs)
    return dict(A1=a1, A2=a2, A3=a3), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'int64')
    b2, offs = parse(buf, offs, 'uint32')
    return dict(B1=b1, B2=b2), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'int64')
    c2_size, offs = parse(buf, offs, 'uint16')
    c2_offs, offs = parse(buf, offs, 'uint32')
    c2 = []
    for _ in range(c2_size):
        val, c2_offs = parse(buf, c2_offs, 'char')
        c2.append(val.decode())
    c3, offs = parse(buf, offs, 'float')
    c4_size, offs = parse(buf, offs, 'uint16')
    c4_offs, offs = parse(buf, offs, 'uint16')
    c4 = []
    for _ in range(c4_size):
        val, c4_offs = parse(buf, c4_offs, 'uint32')
        c4.append(val)
    c5, offs = parse(buf, offs, 'uint16')
    c6, offs = parse(buf, offs, 'uint64')
    return dict(C1=c1, C2=''.join(c2), C3=c3, C4=c4, C5=c5, C6=c6), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'int64')
    d2, offs = parse(buf, offs, 'uint16')
    d3 = []
    for _ in range(4):
        val, offs = parse(buf, offs, 'int32')
        d3.append(val)
    d4, offs = parse(buf, offs, 'double')
    d5, offs = parse(buf, offs, 'float')
    d6, offs = parse(buf, offs, 'int32')
    d7_size, offs = parse(buf, offs, 'uint32')
    d7_offs, offs = parse(buf, offs, 'uint16')
    d7 = []
    for _ in range(d7_size):
        val, d7_offs = parse(buf, d7_offs, 'uint16')
        d7.append(val)
    d8, offs = parse(buf, offs, 'int16')
    return dict(D1=d1, D2=d2, D3=d3, D4=d4,
                D5=d5, D6=d6, D7=d7, D8=d8), offs


def main(buf):
    return parse_a(buf, 5)[0]


if __name__ == "__main__":
    print(main(b'\xb8UUXUt\xca\xca\xa9\xd3Ok4N\x89\xa58\xd9\xe8\xb8p\xf1U\x00\r \xe5\xde'
 b'h\xc3Q\xabZpQ>\xe0\xfa#sB`c\xf5\xfb\xca\xfe\xc4K\x05\x00{\x00\x00\x00\xec'
 b"\x89\x0c?\x02\x00\x80\x00\xca\x045\xd9\x00N\xe0\xe1\x94j\xfbM\xcf+K'\xb8"
 b'\x80\x94\xa68\xf1y.\x13\x92t\x9f\x952m:\x9de\x8e\x81\x902\\\xf7\xcb'
 b'\xbd\xee\xbf\xdc\xb6\xbc\xbd\xf5\xde]\xae\x03\x00\x00\x00\x88\x00(Ybsppd'
 b'\x8b\xc9\xfbC\x08\x16\xca\x81@g_\x90l\xde'))