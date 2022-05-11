import datetime
import mysql.connector
from mysql.connector import errorcode
import dbInfo

try:
       cnx = mysql.connector.connect(**dbInfo.config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees ")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query)
i= 0
for (first_name, last_name, hire_date) in cursor:
    if (hire_date >= hire_start) and  (hire_date <= hire_end): 
        #print("{}, {} was hired on {:%d %b %Y}".format(
    #last_name, first_name, hire_date))
        i += 1
print("Number of Rows =", i)

cursor.close()
