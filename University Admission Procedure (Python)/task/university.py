maximum = int(input())

def filereader(name):
    file = open(name,'r')
    list = []
    for line in file:
        list.append(line.strip().split(" "))
    file.close()
    return list
all = filereader('applicants.txt')

def list_sorter(major, list):
    if major == "Physics":
        list.sort(key=lambda x: (-max(float(x[6]),((float(x[2]) + float(x[4])) / 2)), x[0], x[1], x[3]))
    elif major == "Chemistry" :
        list.sort(key=lambda x: (-max(float(x[6]),float(x[3])), x[0], x[1], x[3]))
    elif major == "Mathematics":
        list.sort(key=lambda x: (-max(float(x[6]),float(x[4])), x[0], x[1], x[3]))
    elif major == "Biotech":
        list.sort(key=lambda x: (-max(float(x[6]),((float(x[2])) + float(x[3])) / 2), x[0], x[1], x[3]))
    else:
        list.sort(key=lambda x: (-max(float(x[6]),((float(x[4]) + float(x[5])) / 2)), x[0], x[1], x[3]))
selected = []

def priority_filter(major,list,rank,now):
    list_sorter(major, list)
    new_list = now
    for stu_info in list:
        first = stu_info[rank + 6]
        if first == major and len(new_list) < maximum and stu_info not in selected:
            new_list.append(stu_info)
            selected.append(stu_info)
    return new_list

def printer(major, list):
    list_sorter(major, list)
    name_file = open("{}.txt".format(major.lower()), 'w', encoding = 'utf-8')
    for n in list:
        accepted = n
        first = accepted[0]
        last = accepted[1]
        if major == "Physics":
            gpa = max(float(accepted[6]),(float(accepted[2])+ float(accepted[4])) / 2)
        elif major == "Chemistry":
            gpa = max(float(accepted[6]),float(accepted[3]))
        elif major == "Mathematics":
            gpa = max(float(accepted[6]),float(accepted[4]))
        elif major == "Biotech":
            gpa = max(float(accepted[6]),(float(accepted[3]) + float(accepted[2])) / 2)
        else:
            gpa = max(float(accepted[6]),(float(accepted[4]) + float(accepted[5])) / 2)
        name_file.write("{} {} {}".format(first, last , gpa) + '\n')
    print()

uni = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
for n in range(1,4):
    for key,value in uni.items():
        uni[key] = priority_filter(key,all,n,value)
for key,value in uni.items():
    printer(key,value)