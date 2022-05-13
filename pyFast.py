import datetime
import mysql.connector
import sys
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

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

names =[]
for (first_name, last_name, hire_date) in cursor:
    names.append(first_name)
    
lenNames = len(names)
next if (lenNames != 0) else sys.exit("no Values in query")
print("Rows returned from query:", cursor.rowcount)
print("Number of Rows affected =", lenNames)
print("Last Name in List: ", names[lenNames-1])

cursor.close()

