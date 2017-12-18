from Dao import FirstLayer
from Dao import DepartmHandResult
from tool import ConvertTime

# print("_____________________________________")
# FirstLayer.first_layer("2016","03","22","2017","09","11")
def testTime():
    list = ConvertTime.convertTime("2016","03","22","2017","09","11")
    for i in list:
        print(i)

testTime()