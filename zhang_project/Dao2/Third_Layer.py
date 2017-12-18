# -*- coding: UTF-8 -*-

import cx_Oracle
import os
import sys



def Third_layer(dateBegin, dateEnd,Responsbl_Type,Employee_Code):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    if dateBegin == None:
        dateBegin = '2017-07-22'
        dateEnd = '2017-08-23'
        Responsbl_Type = '服务质量卡'
        Employee_Code = '客运车间'
    print(dateBegin,dateEnd,Responsbl_Type,Employee_Code)
    try:
        conn = cx_Oracle.connect("MASTER/123456@172.21.176.40/XE")
    except Exception:
        print("数据库连接出错",Exception)
        conn.close()
        sys.exit(1)
    sql = "SELECT * FROM (SELECT S_EMPLOYEECODE,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='"
    sql_1 = sql + dateBegin + "'" + "AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='"
    sql_2 = sql_1 + dateEnd + "'" + "AND S_HANDLEREASULT='"
    sql_3 = sql_2 + Responsbl_Type + "'" + "AND S_RESPONSIBILITYDEPT='"
    sql_4 = sql_3 + Employee_Code + "'"+ "GROUP BY S_EMPLOYEECODE) t ORDER BY t.count DESC"
    sqltest = "SELECT * FROM (SELECT S_EMPLOYEECODE,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='2017-07-22' AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='2017-08-23' AND S_HANDLEREASULT = '服务质量卡' AND S_RESPONSIBILITYDEPT='客运车间' GROUP BY S_EMPLOYEECODE) t ORDER BY t.count DESC"
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
    print(dic_a)
    c.close()
    conn.close()
    return dic_a,Employee_Code
