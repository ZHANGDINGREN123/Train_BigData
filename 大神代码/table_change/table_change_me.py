import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

#读取数据
conn = cx_Oracle.connect("MASTER/123456@172.21.176.119/XE")
c = conn.cursor()
c = conn.cursor()
c.execute("SELECT * FROM S_SECURITY_CHECK")
a = c.fetchall()
data = pd.DataFrame(a)
# print(data)

# 读取列名 并设置
c.execute("select COLUMN_NAME from all_col_comments where TABLE_NAME ='S_SECURITY_CHECK'")
column_name = c.fetchall()
column = [x[0] for x in column_name]
data.columns=column
# print(data)

# 选取2017年8月份的数据
data["year"] = data["D_CHECKDATE"].map(lambda x:x.year)
data["month"] = data["D_CHECKDATE"].map(lambda x:x.month)
filter_data = data[data["year"]==2017][data["month"]==8]
filter_data.drop(["month","year"],axis=1,inplace=True)

# 查看发卡类别计数
handler_result_value_counts = filter_data["S_HANDLEREASULT"].value_counts().to_dict()
# print(handler_result_value_counts)

# 违反条款的打头字母计数
pattern = re.compile("\D+")
def match_word(s):
    m = re.search(pattern, s)
    if m is not None:
        return m.group()
    else:
        return None
risk_point_value_counts=filter_data["S_RISKPOINT"].map(match_word).value_counts().to_dict()
print(risk_point_value_counts)
