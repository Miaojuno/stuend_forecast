import csv

import fore_point

def create_stu_point_dict():
    csvfile = open(r'F:\Date\student\raw_data.csv')
    rawdata = csv.reader(csvfile)

    qst2point_dict=fore_point.create_qst2point_dict()
    stu_point_dict={}
    for i, it in enumerate(rawdata):
        try:
            points = qst2point_dict[it[4]]
            for point in points:
                # 元组（student_id，point）作为key
                if (it[3],point) not in stu_point_dict:
                    if eval(it[5]) == 3:
                        do_flag = 1.5
                    else:
                        do_flag = eval(it[5])
                    stu_point_dict[(it[3],point)] = {0: do_flag, 1: 1}  # {do_flag总值,题目数}
                else:
                    if eval(it[5]) == 3:
                        do_flag = 1.5
                    else:
                        do_flag = eval(it[5])
                    stu_point_dict[(it[3],point)][0] += do_flag
                    stu_point_dict[(it[3],point)][1] += 1
        except:
            pass
    return stu_point_dict

def write_stu_point_dict():
    stu_point_dict=create_stu_point_dict()
    pd = open(r'F:\Date\student\stu_point_dict.csv', 'w', newline='')
    stu_point_dict_write = csv.writer(pd)
    for key in stu_point_dict.keys():
        ll = []
        ll.append(key)
        for key2 in stu_point_dict[key]:
            ll.append(key2)
            ll.append(stu_point_dict[key][key2])
        stu_point_dict_write.writerow(ll)
    pd.close()
    print('write stu_point_dict ok')

def read_stu_point_dict():
    reader = open(r'F:\Date\student\stu_point_dict.csv')
    file=csv.reader(reader)
    stu_point_dict={}
    for i,it in enumerate(file):
        idict={}
        lens=len(it)/2
        for j in range(int(lens)):
            idict[eval(it[j*2+1])]=eval(it[j*2+2])
        stu_point_dict[eval(it[0])]=idict
    reader.close()
    return stu_point_dict

# stu_point_dict=read_stu_point_dict()
# mylist=[0,0,0]
# for key in stu_point_dict.keys():
#     ll=stu_point_dict[key]
#     mylist[0] += ll[0]
#     mylist[1] += ll[1]
#     mylist[2] += 1
#
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])