from datetime import datetime
import algorithm
import crud
from datetime import datetime
from datetime import date

def putAdsToDB():

    dictAd1 = {"adId" : 1, "timeStampStart": 1545730073, "timeStampFinish": 1545730103, "name": "persil"}
    dictAd2 = {"adId" : 1, "timeStampStart": 1545740073, "timeStampFinish": 1545740103, "name": "persil"}
    dictAd3 = {"adId" : 2, "timeStampStart": 1545740063, "timeStampFinish": 1545740072, "name": "lenor"}

    adsList = []

    adsList.append(dictAd2)
    adsList.append(dictAd3)
    #

    for dictAd in adsList:
        thistuple = tuple((dictAd["adId"], datetime.fromtimestamp((dictAd["timeStampStart"])),
                           datetime.fromtimestamp((dictAd["timeStampFinish"])),
                           dictAd["name"]))
        tupleList = [thistuple]
        crud.insertAdsRecords(tupleList)









    # dt_objectStart1 = datetime.fromtimestamp(dictAd1["timeStampStart"])
    # dt_objectFinish1 = datetime.fromtimestamp(dictAd1["timeStampFinish"])
    # print(dt_objectStart1)
    # print(dt_objectFinish1)

    # dt_carObjectStart1 = datetime.fromtimestamp(dictCar1["timeStampStart"])
    # print(dt_carObjectStart1)
    #dt_carObjectFinish2 = datetime.fromtimestamp(dictCar1["timeStampFinish"])
    # print(dt_carObjectFinish2)
    # print("----------")

# dictAd1 = {"adId" : 1, "timeStampStart": 1545730073, "timeStampFinish": 1545730103}
# dictAd2 = {"adId" : 1, "timeStampStart": 1545740073, "timeStampFinish": 1545740103}
# dictAd3 = {"adId" : 2, "timeStampStart": 1545740063, "timeStampFinish": 1545740072}
# dt_objectStart1 = datetime.fromtimestamp(dictAd1["timeStampStart"])
# dt_objectFinish1 = datetime.fromtimestamp(dictAd1["timeStampFinish"])
# print(dt_objectStart1)
# print(dt_objectFinish1)
#
# dt_objectStart2 = datetime.fromtimestamp(dictAd2["timeStampStart"])
# dt_objectFinish2 = datetime.fromtimestamp(dictAd2["timeStampFinish"])
# print(dt_objectStart2)
# print(dt_objectFinish2)
# print("---------")
# adList = []
# adList.append(dictAd2)
# adList.append(dictAd3)
