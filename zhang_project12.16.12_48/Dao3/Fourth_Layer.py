# -*- coding: UTF-8 -*-
#######################################################################
# 给定时间区间参数，查询该时间段内发卡类别计数
#
#
#######################################################################
import cx_Oracle
import os
import sys
from tool import ConvertTime



# 给定参数获取结果，等待前端Request（get/post）传递参数，py调用该方法再response结果
# TODO:时间应该所有方法共用
def Fourth_layer(dateBegin, dateEnd,Responsbl_Type,Employee_Code,People_Depart):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    # People_Depart = '101204'
    if dateBegin == None:
        dateBegin = '2017-07-22'
        dateEnd = '2017-08-23'
        Responsbl_Type = '服务质量卡'
        Employee_Code = '客运车间'
        People_Depart = '101204'
    print(dateBegin,dateEnd,Responsbl_Type,Employee_Code)
    # 连接数据库
    try:
        conn = cx_Oracle.connect("MASTER/123456@172.21.176.40/XE")
    except Exception:
        print("数据库连接出错",Exception)
        conn.close()
        sys.exit(1)
    sql = "SELECT * FROM (SELECT S_RESPONSIBLEPERSON,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='"
    sql_1 = sql + dateBegin + "'" + "AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='"
    sql_2 = sql_1 + dateEnd + "'" + "AND S_HANDLEREASULT='"
    sql_3 = sql_2 + Responsbl_Type + "'" + "AND S_RESPONSIBILITYDEPT='"
    sql_4 = sql_3 + Employee_Code + "'" + "AND S_EMPLOYEECODE='"
    sql_5 = sql_4 + People_Depart + "'" + "GROUP BY S_RESPONSIBLEPERSON) t ORDER BY t.count DESC"
    # sqltest = "SELECT * FROM (SELECT S_RESPONSIBLEPERSON,count(1) AS count FROM S_SECURITY_CHECK WHERE to_char(D_CHECKDATE,'yyyy-mm-dd')>='2017-07-22' AND to_char(D_CHECKDATE,'yyyy-mm-dd')<='2017-08-23' AND S_HANDLEREASULT = '黄通' AND S_EMPLOYEECODE='101204' AND  S_RESPONSIBILITYDEPT='运转车间' GROUP BY S_RESPONSIBLEPERSON) t ORDER BY t.count DESC"
    c = conn.cursor()
    try:
        c.execute(sql_5)
    except Exception as e:
        print("查询数据出错，请检查sql语句/参数",e)
        c.close()
        conn.close()
        sys.exit(1)
    a = c.fetchall()
    dic_a = dict(a)
    print(dic_a)
    # for i in a:
    #     print(i)
    # 数据库以及查询都是资源，使用完了记得关闭资源
    c.close()
    conn.close()
    return dic_a,People_Depart

# if __name__=="__main__":
#     print("main")
#     first_layer()

# 调用方法，test
# 方法还不够健壮，但是这些都可以交给前端（比如用户没有选则完整的日期，或者用户选择的结束日期在开始日期之前）
# Fourth_layer('2017-07-22', '2017-08-23','黄通','运转车间','101204')
