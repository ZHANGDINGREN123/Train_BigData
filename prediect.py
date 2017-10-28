import pandas as pd
import numpy as np
import time
import scipy.stats as st
import matplotlib.pyplot as plt

# 导出Excel并做时间差累计
table = pd.read_excel("guantou.xlsx")
table2 = pd.read_excel("guantou.xlsx")
results = []
time1 = time.strptime(table.ix[0]["D_FAULTHAPPENTIME"], '%Y-%m-%d %H:%M:%S')
time1 = time.mktime(time1)
for i in range(len(table) - 1):
    time2 = time.strptime(table.ix[i + 1]["D_FAULTHAPPENTIME"], '%Y-%m-%d %H:%M:%S')
    time2 = time.mktime(time2)
    result = time2 - time1

    results.append(result / 3600)
time.mktime(time.strptime(table.ix[0]["D_FAULTHAPPENTIME"], '%Y-%m-%d %H:%M:%S'))

# 将时间单位设为100小时
a = range(0, 9400, 100)
t = 0
l = []

# 单位时间累计次数
for j in range(len(a) - 1):
    for i in range(len(results)):
        if 100 * (j + 1) > results[i] > 100 * j:
            # print(results[i])
            t = t + 1
        else:
            continue
    l.append(t)
    if t != 0:
        t = 0

# print(results[i])
# print(l)

# j记录一下在100小时间隔内发生故障0，1，2，3的次数累计
b = 0.0
c = 0.0
d = 0.0
e = 0.0
for r in range(len(l)):

    if (l[r] == 0):
        e = e + 1
    # print('e=', e)
    if (l[r] == 1):
        b = b + 1
    # print('b=', b)
    if (l[r] == 2):
        c = c + 1

    # print("c=", c)
    if (l[r] == 3):
        d = d + 1

        # print('d=', d)

# 计算未分组情况下的lmbda的值
# number = [59.0, 26.0, 6.0, 2.0]
number = [e, b, c, d]
lmbda = sum(x * y for x, y in zip(range(4), number)) / sum(number)
print(lmbda)
# 计算故障发生周期
Day_fault = 1 / lmbda * 100 / 24  # 1/x=lmbda/100
print(Day_fault)

rv = st.poisson(lmbda)
# number = [59.0, 26.0, 6.0, 2.0]
number = [e, b, c, d]
x = range(4)
plt.bar(np.array(x), number, width=0.3, label='Observed values')
plt.plot(x, sum(number) * rv.pmf(x), ls='dashed',
         lw=2, c='r', label='Poisson distribution\n$(\lambda)$')
plt.xlim([-1, 3])
plt.ylim([0, 60])
plt.xlabel('times of fault in 100 hours')
plt.ylabel('the cumulant of times')
plt.legend(loc='best')
plt.show()  # 做泊松分布的拟合图
