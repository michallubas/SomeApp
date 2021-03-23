from datetime import datetime
import algorithm
import crud
from datetime import datetime
from datetime import date


def putCarsToDB():
    dictCar1 = {"carId": 1, "timeStampStart": 1545740083, "timeStampFinish": 1545740113, "numbViewers": 30.0}
    dictCar2 = {"carId": 2, "timeStampStart": 1545740073, "timeStampFinish": 1545740102, "numbViewers": 3.0}
    dictCar3 = {"carId": 3, "timeStampStart": 1545740063, "timeStampFinish": 1545740083, "numbViewers": 20.0}
    dictCar4 = {"carId": 4, "timeStampStart": 1545740058, "timeStampFinish": 1545740118, "numbViewers": 100.0}

    carList = []
    carList.append(dictCar1)
    carList.append(dictCar2)
    carList.append(dictCar3)
    carList.append(dictCar4)

    for dictCar in carList:
        thistuple = tuple((dictCar["carId"], datetime.fromtimestamp((dictCar["timeStampStart"])),
                           datetime.fromtimestamp((dictCar["timeStampFinish"])),
                           dictCar["numbViewers"]))
        tupleList = [thistuple]
        crud.insertVehicleRecords(tupleList)










# dictCar1 = {"carId" : 1, "timeStampStart": 1545740083, "timeStampFinish": 1545740113, "numbViewers": 30.0}
# dictCar2 = {"carId" : 2, "timeStampStart": 1545740073, "timeStampFinish": 1545740102, "numbViewers": 3.0}
# dictCar3 = {"carId" : 3, "timeStampStart": 1545740063, "timeStampFinish": 1545740083, "numbViewers": 20.0}
# dictCar4 = {"carId" : 4, "timeStampStart": 1545740058, "timeStampFinish": 1545740118, "numbViewers": 100.0}
#
# dt_carObjectStart1 = datetime.fromtimestamp(dictCar1["timeStampStart"])
# print(dt_carObjectStart1)
# dt_carObjectFinish2 = datetime.fromtimestamp(dictCar1["timeStampFinish"])
# print(dt_carObjectFinish2)
# print("----------")
#
# carList = []
# carList.append(dictCar1)
# carList.append(dictCar2)
# carList.append(dictCar3)
# carList.append(dictCar4)