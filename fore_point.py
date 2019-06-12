import csv


def create_qst2point_dict():
    qst2point_dict = {}
    file = open(r'F:\Date\student\topics.txt')
    for i,it in enumerate(file.readlines()):
        ll = it.strip().split('\t')
        key = ll[0]
        ll = list(map(int, ll[1:]))
        qst2point_dict[key]=ll
    return qst2point_dict

def create_point_dict():
    csvfile = open(r'F:\Date\student\raw_data.csv')
    rawdata = csv.reader(csvfile)

    qst2point_dict=create_qst2point_dict()
    point_dict={}
    for i, it in enumerate(rawdata):
        try:
            points = qst2point_dict[it[4]]
            for point in points:
                if point not in point_dict:
                    if eval(it[5]) == 3:
                        do_flag = 1.5
                    else:
                        do_flag = eval(it[5])
                    point_dict[point] = {0: do_flag, 1: 1}  # {do_flag总值,题目数}
                else:
                    if eval(it[5]) == 3:
                        do_flag = 1.5
                    else:
                        do_flag = eval(it[5])
                    point_dict[point][0] += do_flag
                    point_dict[point][1] += 1
        except:
            pass
    return point_dict

# 11191352 知识点对应关系不存在个数 约2/3
# 15063.327895595432 拥有知识点题目的知识点难度总和
# 11014.908646003263 拥有知识点题目个数

def write_point_dict():
    point_dict=create_point_dict()
    pd = open(r'F:\Date\student\point_dict.csv', 'w', newline='')
    point_dict_write = csv.writer(pd)
    for key in point_dict.keys():
        ll = []
        ll.append(key)
        for key2 in point_dict[key]:
            ll.append(key2)
            ll.append(point_dict[key][key2])
        point_dict_write.writerow(ll)
    pd.close()
    print('write point_dict ok')

def read_point_dict():
    reader = open(r'F:\Date\student\point_dict.csv')
    file=reader.readlines()
    point_dict={}
    for i,it in enumerate(file):
        it=it.strip().split(',')
        idict={}
        lens=len(it)/2
        for j in range(int(lens)):
            idict[eval(it[j*2+1])]=eval(it[j*2+2])
        point_dict[eval(it[0])]=idict
    reader.close()
    return point_dict

