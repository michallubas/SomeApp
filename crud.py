from mysql.connector import connect,Error
from datetime import datetime

def insertVehicleRecords(tupleList,chosenDatabase="test_records"):
    try:
        with connect(host="localhost",
        user="root",
        password="admin",
        database=chosenDatabase
        ) as connection:

            insert_vehicle_records_query = """
                        INSERT INTO vehicle_records
                        (vehicle_Id, timeStampStart , timeStampFinish, numb )
                        VALUES (%s, %s, %s, %s)
                        """

            with connection.cursor() as cursor:
                cursor.executemany(insert_vehicle_records_query, tupleList)
                connection.commit()

    except Error as e:
        print(e)

def insertAdsRecords(tupleList,chosenDatabase="test_records"):
    try:
        with connect(host="localhost",
        user="root",
        password="admin",
        database=chosenDatabase
        ) as connection:

            insert_vehicle_records_query = """
                        INSERT INTO ads_records
                        (adId, timeStampStart , timeStampFinish, name )
                        VALUES (%s, %s, %s, %s)
                        """

            with connection.cursor() as cursor:
                cursor.executemany(insert_vehicle_records_query, tupleList)
                connection.commit()

    except Error as e:
        print(e)

def readAdsRecords(tableToRead,chosenDatabase="test_records"):
    try:
        with connect(host="localhost",
        user="root",
        password="admin",
        database=chosenDatabase
        ) as connection:

            read_ads_records_query = """
            SELECT * from (%s)
            """ % (tableToRead)


            with connection.cursor() as cursor:
                list = []
                cursor.execute(read_ads_records_query)
                result = cursor.fetchall()
                for row in result:
                    tempDict = { "adId":row[1], "timeStampStart": datetime.timestamp(row[2]), "timeStampFinish": datetime.timestamp(row[3]), "name": row[4]}
                    list.append(tempDict)
                return list

    except Error as e:
        print("ddd")
        print(e)

def readCarsRecords(tableToRead,chosenDatabase="test_records"):
    try:
        with connect(host="localhost",
        user="root",
        password="admin",
        database=chosenDatabase
        ) as connection:

            read_ads_records_query = """
            SELECT * from (%s)
            """ % (tableToRead)


            with connection.cursor() as cursor:
                list = []
                cursor.execute(read_ads_records_query)
                result = cursor.fetchall()
                for row in result:
                    tempDict = { "carId":row[1], "timeStampStart": datetime.timestamp(row[2]), "timeStampFinish": datetime.timestamp(row[3]), "numbViewers": row[4]}
                    list.append(tempDict)
                return list

    except Error as e:
        print("ddd")
        print(e)