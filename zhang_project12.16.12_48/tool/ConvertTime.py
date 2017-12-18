def convertTime(yearB, monthB, dayB,yearE, monthE, dayE ):
    list = []
    dateBegin = yearB + "-" + monthB + "-" + dayB
    dateEnd = yearE + "-" + monthE + "-" + dayE
    list.append(dateBegin)
    list.append(dateEnd)
    # print(type(list[0]))
    return list
    # print(dateBegin,dateEnd)
convertTime("2017","05","22","2017","08","23")
# list1 = convertTime("2017","05","22","2017","08","23")
# print(list1)