#coding=utf-8

from flask import Flask,render_template,request
from Dao import FirstLayer
from Dao import DepartmHandResult
from Dao1 import Second_Layer,Second_DepartmHandResult
from Dao2 import Third_Layer,Third_DepartmHandResult
from Dao3 import Fourth_Layer,Fourth_DepartmHandResult
from Table_Show import Security_Table_Show,Fault_Table_Show
from Word_Cloud import security_word_cloud,falut_word_cloud

app = Flask(__name__)

@app.route('/index',methods=['GET', 'POST'])
def index():
    if request == 'GET':
        return render_template("index.html")
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        Hand_Result = request.form.get('Hand_Result')
        EmployerCode = request.form.get('Department_Type')
        Responsibli_Preson = request.form.get('Responsibli_Preson')
        Show_S_RESPONSIBILITYDEPT = DepartmHandResult.first_layer_Two('2017-07-22', '2017-08-23')
        show_S_HANDLEREASULT = FirstLayer.first_layer(dateBegin,dateEnd)
        show_S_Second_Layer_RESPONSIBILITYDEPT,show_S_Second_Layer_Hand_Result= Second_Layer.Second_layer(dateBegin,dateEnd,Hand_Result)
        show_S_Third_Layer_S_EMPLOYEECODE,show_S_Third_Layer_EmployerCode= Third_Layer.Third_layer(dateBegin,dateEnd,Hand_Result,EmployerCode)
        show_S_Fourth_Layer_RESPONSIBLEPERSON,show_S_Fourth_Layer_People_Depart = Fourth_Layer.Fourth_layer(dateBegin,dateEnd,Hand_Result,EmployerCode,Responsibli_Preson)
        return render_template('index.html',dateBegin = dateBegin,
                               dateEnd = dateEnd,
                               Show_S_RESPONSIBILITYDEPT = Show_S_RESPONSIBILITYDEPT, show_S_HANDLEREASULT = show_S_HANDLEREASULT,show_S_Second_Layer_RESPONSIBILITYDEPT = show_S_Second_Layer_RESPONSIBILITYDEPT,show_S_Second_Layer_Hand_Result = show_S_Second_Layer_Hand_Result,show_S_Third_Layer_S_EMPLOYEECODE = show_S_Third_Layer_S_EMPLOYEECODE,show_S_Third_Layer_EmployerCode=show_S_Third_Layer_EmployerCode,show_S_Fourth_Layer_RESPONSIBLEPERSON = show_S_Fourth_Layer_RESPONSIBLEPERSON,show_S_Fourth_Layer_People_Depart=show_S_Fourth_Layer_People_Depart)


@app.route('/init',methods=['GET', 'POST'])
def init():
    if request == 'GET':
        return render_template("init1.html")
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        Hand_Result = request.form.get('Hand_Result')
        EmployerCode = request.form.get('Department_Type')
        Responsibli_Preson = request.form.get('Responsibli_Preson')
        Show_S_RESPONSIBILITYDEPT = DepartmHandResult.first_layer_Two(dateBegin, dateEnd)
        show_S_HANDLEREASULT = FirstLayer.first_layer(dateBegin, dateEnd)
        show_S_Second_Layer_RESPONSIBILITYDEPT = Second_Layer.Second_layer(dateBegin, dateEnd, Hand_Result)
        show_S_Third_Layer_S_EMPLOYEECODE = Third_Layer.Third_layer(dateBegin, dateEnd, Hand_Result, EmployerCode)
        show_S_Fourth_Layer_RESPONSIBLEPERSON = Fourth_Layer.Fourth_layer(dateBegin, dateEnd, Hand_Result, EmployerCode,
                                                                          Responsibli_Preson)
        return render_template('init1.html',Show_S_RESPONSIBILITYDEPT=Show_S_RESPONSIBILITYDEPT,
                               show_S_HANDLEREASULT=show_S_HANDLEREASULT,
                               show_S_Second_Layer_RESPONSIBILITYDEPT=show_S_Second_Layer_RESPONSIBILITYDEPT,
                               show_S_Third_Layer_S_EMPLOYEECODE=show_S_Third_Layer_S_EMPLOYEECODE,
                               show_S_Fourth_Layer_RESPONSIBLEPERSON=show_S_Fourth_Layer_RESPONSIBLEPERSON)
@app.route('/index2',methods=['GET', 'POST'])
def index2():
    if request == 'GET':
        return render_template("index.html")
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        Show_S_RESPONSIBILITYDEPT = DepartmHandResult.first_layer_Two(dateBegin, dateEnd)
        Check_Department = request.form.get('Check_Department')
        Hand_Result = request.form.get('Hand_Result')
        Responsibli_Code_two = request.form.get('Responsibli_Code_two')
        show_S_Second_Layer_Two_Check_Department,show_S_Second_Layer__Two_Check_Department1= Second_DepartmHandResult.Second_Layer_Two(dateBegin, dateEnd,Check_Department)
        show_S_Third_Layer_S_Hand_Result,show_S_Third_Layer_S_Hand_Result1= Third_DepartmHandResult.Third_Layer_Two(dateBegin,dateEnd,Check_Department,Hand_Result)
        show_S_Fourth_Layer_People_Code,show_S_Fourth_Layer_People_Code1 = Fourth_DepartmHandResult.Fourth_Layer_Two(dateBegin,dateEnd,Check_Department,Hand_Result,Responsibli_Code_two)
        # return render_template('index2.html',Show_S_RESPONSIBILITYDEPT = Show_S_RESPONSIBILITYDEPT, show_S_HANDLEREASULT = show_S_HANDLEREASULT,show_S_Second_Layer_RESPONSIBILITYDEPT = show_S_Second_Layer_RESPONSIBILITYDEPT,show_S_Second_Layer_Hand_Result = show_S_Second_Layer_Hand_Result,show_S_Third_Layer_S_EMPLOYEECODE = show_S_Third_Layer_S_EMPLOYEECODE,show_S_Third_Layer_EmployerCode=show_S_Third_Layer_EmployerCode,show_S_Fourth_Layer_RESPONSIBLEPERSON = show_S_Fourth_Layer_RESPONSIBLEPERSON,show_S_Fourth_Layer_People_Depart=show_S_Fourth_Layer_People_Depart)
        return render_template('index2.html',dateBegin = dateBegin,
                               dateEnd = dateEnd,
                               Show_S_RESPONSIBILITYDEPT = Show_S_RESPONSIBILITYDEPT,
                               show_S_Second_Layer_Two_Check_Department = show_S_Second_Layer_Two_Check_Department,
                               show_S_Second_Layer__Two_Check_Department1 = show_S_Second_Layer__Two_Check_Department1,
                               show_S_Third_Layer_S_Hand_Result = show_S_Third_Layer_S_Hand_Result,
                               show_S_Third_Layer_S_Hand_Result1 = show_S_Third_Layer_S_Hand_Result1,
                               show_S_Fourth_Layer_People_Code = show_S_Fourth_Layer_People_Code,
                               show_S_Fourth_Layer_People_Code1 = show_S_Fourth_Layer_People_Code1)

@app.route('/',methods=['GET', 'POST'])
def faultyDashboard():
    if request == 'GET':
        return render_template("faultyDashboard.html")
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        show_S_Security_Word = security_word_cloud.Security_Word_Cloud(dateBegin,dateEnd)
        show_S_Falut_Word = falut_word_cloud.Fault_Word_Cloud(dateBegin,dateEnd)
    return render_template('faultyDashboard.html',
                           show_S_Security_Word = show_S_Security_Word,
                           show_S_Falut_Word = show_S_Falut_Word)


@app.route('/securityDashboard')e
def securityDashboard():
    return render_template('securityDashboard.html')

@app.route('/punchDashboard',)
def punchDashboard():
    return render_template('punchDashboard.html')

@app.route('/tableFault',methods=['GET', 'POST'])
def tableFault():
    if request == 'GET':
        return render_template("faultyDashboard.html")
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        show_S_Fault_Table = Fault_Table_Show.fault_table_show(dateBegin, dateEnd)
    return render_template('table_fault.html',
                           show_S_Fault_Table=show_S_Fault_Table)

@app.route('/tableSecurity',methods=['GET', 'POST'])
def tableSecurity():
    if request == 'GET':
        return render_template("faultyDashboard.html")
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        show_S_Security_Table = Security_Table_Show.security_table_show(dateBegin,dateEnd)
    return render_template('table_security.html',
                           show_S_Security_Table = show_S_Security_Table)

@app.route('/tablePunch',)
def tablePunch():
    return render_template('table_punch.html')



if __name__ == '__main__':
    app.run(debug=True,host='172.21.176.74',port=5000)