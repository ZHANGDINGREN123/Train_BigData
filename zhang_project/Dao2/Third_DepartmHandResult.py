# -*- coding: UTF-8 -*-

import cx_Oracle
import os
import sys


def Third_Layer_Two(dateBegin, dateEnd,Check_Department,Pull_HandResult):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    if dateBegin == None:
        dateBegin = '2017-07-22'
        dateEnd = '2017-08-23'
        Check_Department = '站领导'
        Pull_HandResult = '红通'

    try:
        conn = cx_Oracle.connect("MASTER/123456@172.21.176.40/XE")
    except Exception:
        print("数据库连接出错",Exception)
        conn.close()
        sys.exit(1)
    sql = "SELECT * FROM (SELECT S_CHECKPERSON,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='"
    sql_1 = sql + dateBegin + "'" + "AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='"
    sql_2 = sql_1 + dateEnd + "'" + "AND S_CHECKDEPARTMENT = '"
    sql_3 = sql_2 + Check_Department + "'" + "AND S_HANDLEREASULT = '"
    sql_4 = sql_3 + Pull_HandResult + "'" + "GROUP BY S_CHECKPERSON) t ORDER BY t.count DESC"
    sqltest = "SELECT * FROM (SELECT S_EMPLOYEECODE,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='2017-07-22' AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='2017-08-23' AND S_CHECKDEPARTMENT = '站领导' AND S_HANDLEREASULT = '红通' GROUP BY S_EMPLOYEECODE) t ORDER BY t.count DESC"
    c = conn.cursor()
    try:
        c.execute(sql_4)
    except Exception as e:
        print("查询数据出错，请检查sql语句/参数",e)
        c.close()
        conn.close()
        sys.exit(1)
    a = c.fetchall()
    dic_a = dict(a)
    c.close()
    conn.close()
    return dic_a,Pull_HandResult
