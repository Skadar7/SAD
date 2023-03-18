import re


def main(source):
    res = {}
    s = []
    for i in re.findall(r'\w+["]*\s*==>\s*\w+[_]*\d+', source):
        vk = re.split(r'==>', i)
        print(vk)
        if vk[0].strip() in res:
            s.append(vk[1].strip())
            res[vk[0].strip()] += s
            s.clear()
        else:
            res.setdefault(vk[0].strip(), []).append(vk[1].strip())
    return res



if __name__ == "__main__":
    print(main('\\begin .do val @"vequti" ==> tesole_759 .end, .do val @"tiinbi'
               '==>orveon_312 .end, .do val @"rea_659" ==>enla_132 .end, \end vequti" ==> qqq_759'))