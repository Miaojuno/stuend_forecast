import csv

# id   teacher_id   homework_id   student_id   qst_id   do_flag   this_time
# 0        1            2             3           4        5          6

# 0:id 1:flag 2:teacher_level 3:teacher_num 4:homework_dif 5:homework_num
# 6:student_level 7:student_num 8:student_current_level 9:student_current_num
# 10:qst_dif 11:qst_num 12:point_dif 13:point_num(该题涉及的知识点个数) 14:stu_point_level 15:stu_point_num

# 返回时间段
import fore_point
import fore_stu_point


def find_time_stamp(this_time):
    this_time=eval(this_time)
    if this_time<20171131:
        return 1
    elif this_time<20180231:
        return 2
    elif this_time<20180531:
        return 3
    else:
        return 4


# 创建字典
def create_dict():
    csvfile = open(r'F:\Date\student\raw_data.csv')
    rawdata = csv.reader(csvfile)
    teache_dict = {}
    homework_dict = {}
    qst_dict = {}
    student_dict={}

    for i, it in enumerate(rawdata):

        # create teacher_dict
        if it[1] not in teache_dict:
            if eval(it[5]) == 3:
                do_flag = 1.5
            else:
                do_flag = eval(it[5])
            teache_dict[it[1]] = {0: do_flag, 1: 1}  # {do_flag总值,题目数}
        else:
            if eval(it[5]) == 3:
                do_flag = 1.5
            else:
                do_flag = eval(it[5])
            teache_dict[it[1]][0] += do_flag
            teache_dict[it[1]][1] += 1

        # create homework_dict
        if it[2] not in homework_dict:
            if eval(it[5]) == 3:
                do_flag = 1.5
            else:
                do_flag = eval(it[5])
            homework_dict[it[2]] = {0: do_flag, 1: 1}  # {do_flag总值,题目数}
        else:
            if eval(it[5]) == 3:
                do_flag = 1.5
            else:
                do_flag = eval(it[5])
            homework_dict[it[2]][0] += do_flag
            homework_dict[it[2]][1] += 1

        # create qst_dict
        if it[4] not in qst_dict:
            if eval(it[5]) == 3:
                do_flag = 1.5
            else:
                do_flag = eval(it[5])
            qst_dict[it[4]] = {0: do_flag, 1: 1}  # {do_flag总值,题目数}
        else:
            if eval(it[5]) == 3:
                do_flag = 1.5
            else:
                do_flag = eval(it[5])
            qst_dict[it[4]][0] += do_flag
            qst_dict[it[4]][1] += 1

        # create student_dict
        if it[3] not in student_dict:
            if eval(it[5]) == 3:
                do_flag = 1.5
            else:
                do_flag = eval(it[5])
            time_stamp=find_time_stamp(it[6])
            student_dict[it[3]] = {0: do_flag, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            student_dict[it[3]][time_stamp * 2] += do_flag
            student_dict[it[3]][time_stamp * 2 + 1] += 1
        else:
            if eval(it[5]) == 3:
                do_flag = 1.5
            else:
                do_flag = eval(it[5])
            time_stamp = find_time_stamp(it[6])
            student_dict[it[3]][0] += do_flag
            student_dict[it[3]][1] += 1
            student_dict[it[3]][time_stamp * 2] += do_flag
            student_dict[it[3]][time_stamp * 2 + 1] += 1

        x = i / 16740574 * 100
        print("create dict---%.2f" % (x) + '%---'+str(i)+"/"+"16740574")

    return teache_dict,homework_dict,qst_dict,student_dict


def write_dict(teache_dict,homework_dict,qst_dict,student_dict):
    td = open(r'F:\Date\student\teache_dict.csv', 'w', newline='')
    teache_dict_write = csv.writer(td)
    for key in teache_dict.keys():
        ll = []
        ll.append(key)
        for key2 in teache_dict[key]:
            ll.append(key2)
            ll.append(teache_dict[key][key2])
        teache_dict_write.writerow(ll)
    td.close()
    print('write teache_dict ok')

    hd = open(r'F:\Date\student\homework_dict.csv', 'w', newline='')
    homework_dict_write = csv.writer(hd)
    for key in homework_dict.keys():
        ll = []
        ll.append(key)
        for key2 in homework_dict[key]:
            ll.append(key2)
            ll.append(homework_dict[key][key2])
        homework_dict_write.writerow(ll)
    hd.close()
    print('write homework_dict ok')

    qd = open(r'F:\Date\student\qst_dict.csv', 'w', newline='')
    qst_dict_write = csv.writer(qd)
    for key in qst_dict.keys():
        ll = []
        ll.append(key)
        for key2 in qst_dict[key]:
            ll.append(key2)
            ll.append(qst_dict[key][key2])
        qst_dict_write.writerow(ll)
    qd.close()
    print('write qst_dict ok')

    sd = open(r'F:\Date\student\student_dict.csv', 'w', newline='')
    student_dict_write = csv.writer(sd)
    for key in student_dict.keys():
        ll = []
        ll.append(key)
        for key2 in student_dict[key]:
            ll.append(key2)
            ll.append(student_dict[key][key2])
        student_dict_write.writerow(ll)
    sd.close()
    print('write student_dict ok')

def read_dict():
    reader = open(r'F:\Date\student\teache_dict.csv')
    file=reader.readlines()
    teache_dict={}
    for i,it in enumerate(file):
        it=it.strip().split(',')
        idict={}
        lens=len(it)/2
        for j in range(int(lens)):
            idict[eval(it[j*2+1])]=eval(it[j*2+2])
        teache_dict[it[0]]=idict
    reader.close()
    reader = open(r'F:\Date\student\homework_dict.csv')
    file = reader.readlines()
    homework_dict = {}
    for i, it in enumerate(file):
        it = it.strip().split(',')
        idict = {}
        lens = len(it) / 2
        for j in range(int(lens)):
            idict[eval(it[j * 2 + 1])] = eval(it[j * 2 + 2])
        homework_dict[it[0]] = idict
    reader.close()
    reader = open(r'F:\Date\student\qst_dict.csv')
    file = reader.readlines()
    qst_dict = {}
    for i, it in enumerate(file):
        it = it.strip().split(',')
        idict = {}
        lens = len(it) / 2
        for j in range(int(lens)):
            idict[eval(it[j * 2 + 1])] = eval(it[j * 2 + 2])
        qst_dict[it[0]] = idict
    reader.close()
    reader = open(r'F:\Date\student\student_dict.csv')
    file = reader.readlines()
    student_dict = {}
    for i, it in enumerate(file):
        it = it.strip().split(',')
        idict = {}
        lens = len(it) / 2
        for j in range(int(lens)):
            idict[eval(it[j * 2 + 1])] = eval(it[j * 2 + 2])
        student_dict[it[0]] = idict
    reader.close()
    return teache_dict,homework_dict,qst_dict,student_dict


def write_rawdata_bp(teache_dict, homework_dict, qst_dict, student_dict,
                     qst2point_dict, point_dict ,stu_point_dict):
    csvfile = open(r'F:\Date\student\raw_data.csv')
    rawdata = csv.reader(csvfile)

    out = open(r'F:\Date\student\raw_data_bp2.csv','w', newline='')
    csv_write = csv.writer(out)


    for i, it in enumerate(rawdata):
        ll=[]
        if eval(it[5]) !=3:
            # id
            ll.append(eval(it[0]))
            # flag
            ll.append(eval(it[5]))
            # teacher
            ll.append(2 - teache_dict[it[1]][0] / teache_dict[it[1]][1])
            ll.append(teache_dict[it[1]][1])
            # homework
            ll.append(homework_dict[it[2]][0] / homework_dict[it[2]][1] - 1)
            ll.append(homework_dict[it[2]][1])
            # student
            ll.append(2 - student_dict[it[3]][0] / student_dict[it[3]][1])
            ll.append(student_dict[it[3]][1])
            time_stamp=find_time_stamp(it[6])
            ll.append(2 - student_dict[it[3]][time_stamp * 2]
                      / student_dict[it[3]][time_stamp * 2+1])
            ll.append(student_dict[it[3]][time_stamp * 2+1])
            # qst
            ll.append(qst_dict[it[4]][0] / qst_dict[it[4]][1] - 1)
            ll.append(qst_dict[it[4]][1])
            # point
            try:
                points = qst2point_dict[it[4]]
                # 知识点难度 知识点个数
                diflist = [0, 0]
                for point in points:
                    dif = point_dict[point][0] / point_dict[point][1] - 1
                    diflist[0] += dif
                    diflist[1] += 1
                diflist[0] = diflist[0] / diflist[1]
            except:
                diflist = [15063.327895595432 / 11014.908646003263 - 1, 1.1920468815403935]
            ll.append(diflist[0])
            ll.append(diflist[1])
            # stu_point_dict
            try:
                points = qst2point_dict[it[4]]
                # 知识点难度 知识点个数
                diflist = [0, 0]
                for point in points:
                    dif = 2 - stu_point_dict[(it[3],point)][0] / stu_point_dict[(it[3],point)][1]
                    diflist[0] += dif
                    diflist[1] += 1
                diflist[0] = diflist[0] / diflist[1]
            except:
                diflist = [ 2 - 9233820 / 6752139 , 0 ]
            ll.append(diflist[0])
            ll.append(diflist[1])

            #write
            csv_write.writerow(ll)

            x = i / 16740574 * 100
            print("write---%.2f" % (x) + '%---' + str(i) + "/" + "16740574")

qst2point_dict = fore_point.create_qst2point_dict()
point_dict = fore_point.read_point_dict()
stu_point_dict = fore_stu_point.read_stu_point_dict()
teache_dict,homework_dict,qst_dict,student_dict = read_dict()

write_rawdata_bp(teache_dict,homework_dict,qst_dict,student_dict,qst2point_dict,point_dict,stu_point_dict)






