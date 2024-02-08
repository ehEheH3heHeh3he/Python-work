import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel(r'data_analysis.xlsx') 
df = pd.DataFrame(data, columns=['Unnamed: 1'])
df2 = pd.DataFrame(data, columns=['Unnamed: 2'])
df3 = pd.DataFrame(data, columns=['การจัดเก็บภาษีบำรุงท้องที่ ครึ่งปีงบประมาณ 2558 จำแนกตามสำนักงานเขต'])

w = np.array([df])
p = np.array([df2])
m = np.array([df3])

print ("ราย :")
print ("sum  =",np.sum(w[0,1:51]))
print ("mean =",np.mean(w[0,1:51]))
print ("min =",np.min(w[0,1:51]))
print ("max =",np.max(w[0,1:51]))

print ("จำนวนเงิน :")
print ("sum  =",np.sum(p[0,1:51]))
print ("mean =",np.mean(p[0,1:51]))
print ("min =",np.min(p[0,1:51]))
print ("max =",np.max(p[0,1:51]))

x = df3.values.tolist()
y = df.values.tolist()
z = df2.values.tolist()
# print('ไรพีดือไไรพ่าอ',y)
x.pop(0)
y.pop(0)
z.pop(0)
x.pop(50)
y.pop(50)
# z.pop(50)
print(type(y))

listx = []
for i in range(50):
    listx.append(x[i][0])
listy = []
for i in range(50):
    listy.append(y[i][0])
# listz = []
# for i in range(50):
#     listy.append(z[i][0])

print(listy)
plt.bar(listx,listy)
plt.xlabel('สำนักงานเขต')
plt.ylabel('ข้อมูลราย')
plt.show()

# plt.bar(listx,listz,color = 'blue',label = 'b',bottom=listy)
# plt.legend()
# plt.xlabel('ehehe')
# plt.ylabel('haha')
# plt.show()
