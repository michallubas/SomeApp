def searchAds(adId,adList,carList):

    suma = 0
    loop=1
    for carObject in carList:
        for adObject in adList:
            if carObject["timeStampStart"]>=adObject["timeStampStart"] and carObject["timeStampFinish"]<=adObject["timeStampFinish"] and adObject["adId"]==adId:
                suma=suma+carObject["numbViewers"]
                #print(str(carObject["numbViewers"])+", loop: "+str(loop)+ ", car id: "+str(carObject["carId"]))
            if carObject["timeStampStart"]>=adObject["timeStampStart"] and carObject["timeStampStart"]<=adObject["timeStampFinish"] and carObject["timeStampFinish"]>adObject["timeStampFinish"] and adObject["adId"]==adId:
                suma=suma + ((adObject["timeStampFinish"] - carObject["timeStampStart"])*carObject["numbViewers"]/(carObject["timeStampFinish"]-carObject["timeStampStart"]))
                #print(str(((adObject["timeStampFinish"] - carObject["timeStampStart"])*carObject["numbViewers"]/(carObject["timeStampFinish"]-carObject["timeStampStart"])))+", loop: "+str(loop)+ ", car id: "+str(carObject["carId"]))
            if carObject["timeStampStart"]<adObject["timeStampStart"] and carObject["timeStampFinish"]>=adObject["timeStampStart"] and carObject["timeStampFinish"]<=adObject["timeStampFinish"] and adObject["adId"]==adId:
                suma=suma + ((carObject["timeStampFinish"] - adObject["timeStampStart"])*carObject["numbViewers"]/(carObject["timeStampFinish"]-carObject["timeStampStart"]))
                #print(str(( (carObject["timeStampFinish"] - adObject["timeStampStart"])*carObject["numbViewers"]/(carObject["timeStampFinish"]-carObject["timeStampStart"])))+", loop: "+str(loop)+ ", car id: "+str(carObject["carId"]))
            if carObject["timeStampStart"]<adObject["timeStampStart"] and carObject["timeStampFinish"]>adObject["timeStampFinish"] and adObject["adId"]==adId:
                suma=suma + ((adObject["timeStampFinish"] - adObject["timeStampStart"])*carObject["numbViewers"]/(carObject["timeStampFinish"]-carObject["timeStampStart"]))
                #print(str(( (adObject["timeStampFinish"] - adObject["timeStampStart"])*carObject["numbViewers"]/(carObject["timeStampFinish"]-carObject["timeStampStart"])))+", loop: "+str(loop)+ ", car id: "+str(carObject["carId"]))
            loop+=1
    print("For ad id: "+str(adId)+" sum of car viewers is "+str(suma))

