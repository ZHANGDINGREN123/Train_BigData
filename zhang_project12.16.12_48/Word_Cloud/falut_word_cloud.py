import pandas as pd
import numpy as np
import re
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import defaultdict
import cx_Oracle
import os
import sys

def Fault_Word_Cloud(dateBegin,dateEnd):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    # People_Depart = '101204'
    if dateBegin == None:
        dateBegin = '2017-07-22'
        dateEnd = '2017-08-23'
    #     Responsbl_Type = '服务质量卡'
    #     Employee_Code = '客运车间'
    #     People_Depart = '101204'
    # print(dateBegin,dateEnd,Responsbl_Type,Employee_Code)
    # 连接数据库
    try:
        conn = cx_Oracle.connect("MASTER/123456@172.21.176.40/XE")
    except Exception:
        print("数据库连接出错",Exception)
        conn.close()
        sys.exit(1)
    sql = "SELECT * FROM (SELECT S_FAULTDESCRIPTION AS count FROM EQ_FAULT WHERE to_char(D_FAULTHAPPENTIME,'yyyy-mm-dd')>='"
    sql_1 = sql + dateBegin + "'" + "AND to_char(D_FAULTHAPPENTIME,'yyyy-mm-dd')<='"
    sql_2 = sql_1 + dateEnd + "'" + "GROUP BY S_FAULTDESCRIPTION) t ORDER BY t.count DESC"
    # sql_3 = sql_2 + Responsbl_Type + "'" + "AND S_RESPONSIBILITYDEPT='"
    # sql_4 = sql_3 + Employee_Code + "'" + "AND S_EMPLOYEECODE='"
    # sql_5 = sql_4 + People_Depart + "'" + "GROUP BY S_FAULTDESCRIPTION) t ORDER BY t.count DESC"
    sqltest = "SELECT * FROM (SELECT S_FAULTDESCRIPTION AS count FROM EQ_FAULT WHERE to_char(D_FAULTHAPPENTIME,'yyyy-mm-dd')>='2017-07-22' AND to_char(D_FAULTHAPPENTIME,'yyyy-mm-dd')<='2017-08-23' GROUP BY S_FAULTDESCRIPTION) t ORDER BY t.count DESC"
    c = conn.cursor()
    try:
        c.execute(sql_2)
    except Exception as e:
        print("查询数据出错，请检查sql语句/参数",e)
        c.close()
        conn.close()
        sys.exit(1)
    a = c.fetchall()
    lines = a
    # lines = lines.tolist()
    # print(type(a))
    # # print(lines)
    clean_lines = []
    # print(clean_lines)
    for sentence in lines:
        if sentence is np.nan:
            continue
        clean_lines.append(re.sub('\d*','',str(sentence)))
    # print(clean_lines[0:10])
    Key_word = []
    for sentence in clean_lines:
        Key_word.append(jieba.analyse.extract_tags(sentence, topK=5, withWeight=False,allowPOS=()))
    # print(Key_word)
    Key = [item for sub_list in Key_word for item in sub_list]
    # print(Key)
    d = {x: Key.count(x) for x in Key}
    # print(d)

    # dic_a = dict(a)
    # print(dic_a)
    # for i in a:
    #     print(i)
    # 数据库以及查询都是资源，使用完了记得关闭资源
    c.close()
    conn.close()
    return d

# e = Fault_Word_Cloud('2017-07-22', '2017-08-23')
# print(e)

