# -*- coding: UTF-8 -*-

import cx_Oracle
import os
import sys



# 给定参数获取结果，等待前端Request（get/post）传递参数，py调用该方法再response结果
# TODO:时间应该所有方法共用
def first_layer(dateBegin, dateEnd):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    if dateBegin == None:
        dateBegin = '2017-07-22'
        dateEnd = '2017-08-23'
    try:
        conn = cx_Oracle.connect("MASTER/123456@172.21.176.40/XE")
    except Exception:
        print("数据库连接出错",Exception)
        conn.close()
        sys.exit(1)
    sql = "SELECT * FROM (SELECT S_HANDLEREASULT,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='"
    sql_1 = sql + dateBegin + "'" + "AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='"
    sql_2 = sql_1 + dateEnd + "'" + "GROUP BY S_HANDLEREASULT) t ORDER BY t.count DESC"
    sqltest = "SELECT * FROM (SELECT S_HANDLEREASULT,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='2017-07-22' AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='2017-08-23'  GROUP BY S_HANDLEREASULT) t ORDER BY t.count DESC"
    c = conn.cursor()
    try:
        c.execute(sql_2)
    except Exception as e:
        print("查询数据出错，请检查sql语句/参数",e)
        c.close()
        conn.close()
        sys.exit(1)
    a = c.fetchall()
    dic_a = dict(a)
    print(dic_a)
    c.close()
    conn.close()
    return dic_a

