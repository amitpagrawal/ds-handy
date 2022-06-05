import mysql.connector
from datetime import datetime
import pandas as pd
import numpy as np
from datetime import timedelta, date

## please fix these input ##

mydb = mysql.connector.connect(user='****', password='****',
                              host='***',
                              database='***',
                              charset='utf8',
                              use_unicode='FALSE',
                              port = 3306)


startDate = date(2015, 1, 7)
endDate = date(2020, 6, 6)
tableName= "employee"
#any date field by which you can segement data on daily basic uniquely 
dateField = "createdAt"


## input section complete

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

for startDate in daterange(startDate, endDate):
     curDateStr = startDate.strftime("%Y-%m-%d")
     nextDate = startDate+datetime.timedelta(days=1)
     nextDateStr = nextDate.strftime("%Y-%m-%d")
     query = "select * from "+ tableName +"where " + dateField + "> '"+ curDateStr +"' and "+ dateField +"< ' " + nextDateStr +"'"
     print(query)
     df = pd.read_sql(query,mydb)
     fileName = "data/"+ tableName + "_"+"curDateStr"+".csv"
     df.to_csv(fileName)
