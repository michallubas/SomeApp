import algorithm
import dataCarsToDB
import dataAdsToDB
import crud

#adding cars to DB
#dataCarsToDB.putCarsToDB()

#adding ads to DB
#dataAdsToDB.putAdsToDB()

#search specific ad by ID in DB with info about car viewers
algorithm.searchAds(1,crud.readAdsRecords("ads_records"),crud.readCarsRecords("vehicle_records"))


#printing
# print(crud.readAdsRecords("ads_records"))
# print(crud.readCarsRecords("vehicle_records"))