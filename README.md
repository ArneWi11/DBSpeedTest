# DBSpeedTest
Simple Test between Python and MySql, to see if Python or SQL "if/where"-Statements are faster.

Requirements: MySql DB and the free employee Dataset:
https://dev.mysql.com/doc/employee/en/employees-installation.html

Dont forget to setup your Database Information in dbInfo.py!

To measure the execution time, use the following command:

time python3 python.py 

example:

    input:
        $ time python3 pyFast.py

    output:
        Number of Rows affected = 1514
        Last Name in List:  Hilari

        real    0m0,223s
        user    0m0,121s
        sys     0m0,017s
