import pandas as pd
from test25 import getatten

data = getatten()   # get attendance data
j = tuple()
for i in data:
    j = ("USN",) + i[1::3] + ("Average",)
    # print(j)
attendance = pd.DataFrame(columns=j)   #initialize attendence datagram
# print(attendance)

info = []
for i in data:
    info.clear()
    info.insert(0, i[0])
    # print(i)
    a = i[3::3]  # attended classes
    b = i[2::3]  # total classes
    k = 0
    # print(a)
    # print(b)
    for j in a:
        tup = str(j) + "/" + str(b[k])
        info.append(tup)            #info is single list of single student
        k += 1
    # print(info)
#     #average value
    sum_attended,sum_total = 0,0
    for m in a:
        sum_attended = m + sum_attended
    # print(sum_attended)
    for n in b:
        sum_total = n + sum_total
    average = (sum_attended/sum_total)*100
    # print(average)
    info.append(round(average,2))
    # print(info)
    attendance.loc[len(attendance)] = info
    # print(attendance)

print(attendance)
attendance.to_excel("attendence.xlsx", index=False)
