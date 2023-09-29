import pandas as pd
from test25 import getatten

data = getatten()
j = tuple()
for i in data:
    j = ("USN",) + i[1::3]

attendance = pd.DataFrame(columns=j)

ls = []
info = []
for i in data:
    info.clear()
    info.insert(0, i[0])
    b = i[3::3]
    c = i[2::3]
    k = 0
    for j in b:
        tup = str(j) + "/" + str(c[k])
        info.append(tup)
        k += 1
    attendance.loc[len(attendance)] = info

print(attendance)
attendance.to_excel("attendence.xlsx", index=False)
